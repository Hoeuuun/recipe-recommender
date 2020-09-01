MAKEFILE_PATH = $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_FOLDER = $(shell dirname $(MAKEFILE_PATH))

frontend_clean:
	cd frontend && rm -rf node_modules

frontend_install:
	cd frontend && npm install

frontend_up:
	cd frontend && npm start

backend_up:
	cd backend && PYTHONPATH="$(ROOT_FOLDER)" python server.py
