MAKEFILE_PATH = $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_FOLDER = $(shell dirname $(MAKEFILE_PATH))
BACKEND_FLAGS = PYTHONPATH=$(ROOT_FOLDER)

frontend_clean:
	cd frontend && rm -rf node_modules

frontend_install:
	cd frontend && npm install

frontend_up:
	cd frontend && npm start

frontend_build: frontend_install
	cd frontend && PUBLIC_URL='https://hoeunsim.com/rr' npm run-script build
	cp -r frontend/build/ static/

backend_clean:
	cd backend && rm test_*.db

backend_up:
	cd backend && $(BACKEND_FLAGS) python server.py

backend_tests:
	cd backend/tests && $(BACKEND_FLAGS) pytest --cov=backend --cov-report html:htmlcov

#populate_db:
#	cd backend && PYTHONPATH="$(ROOT_FOLDER)" python scrape_DB.py

create_and_populate_db:
	cd backend && PYTHONPATH="$(ROOT_FOLDER)" python create_populate_db.py

copy_over_to_digital_ocean:
	rsync --exclude=venv --exclude=node_modules -rav ../recipe-recommender hoeun@45.55.110.193:~

docker_build: frontend_build
	docker image build -t rr .
	docker run -p 5001:5000 rr

docker_stop:
	docker stop $(docker ps -aq)

docker_remove:
	docker rm $(docker ps -aq)
