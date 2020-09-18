MAKEFILE_PATH = $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_FOLDER = $(shell dirname $(MAKEFILE_PATH))

frontend_clean:
	cd frontend && rm -rf node_modules

frontend_install:
	cd frontend && npm install

frontend_up:
	cd frontend && npm start

frontend_build: frontend_install
	cd frontend && PUBLIC_URL='https://hoeunsim.com/rr' npm run-script build
	cp -r frontend/build/ static/

backend_up:
	cd backend && PYTHONPATH="$(ROOT_FOLDER)" python server.py

#populate_db:
#	cd backend && PYTHONPATH="$(ROOT_FOLDER)" python scrape_DB.py

create_and_populate_db:
	cd backend && PYTHONPATH="$(ROOT_FOLDER)" python create_populate_db.py

copy_over_to_digital_ocean:
	rsync --exclude=venv --exclude=node_modules -rav ../recipe-recommender hoeun@45.55.110.193:~