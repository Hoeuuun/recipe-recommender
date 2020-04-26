frontend_clean:
	cd frontend && rm -rf node_modules

frontend_install:
	cd frontend && npm install

frontend_up:
	cd frontend && npm start

backend_up:
	cd server && python server.py
