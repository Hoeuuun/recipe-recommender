# recipe-recommender

### Getting started
You will need to have these programs installed in your environment:
* [Python 3.7+](https://www.python.org/downloads/)
* [GNU Make](https://www.gnu.org/software/make/)
* [npm 6.14.7](https://www.npmjs.com/package/npm/v/6.14.7)

Get the project code:
```
git clone https://github.com/Hoeuuun/recipe-recommender.git
cd recipe-recommender/
```

Create a Python virtual environment:
```
virtualenv -p $(which python3) venv
source venv/bin/activate
```

Install the dependencies:
```
pip install -r backend/requirements.txt
```

Build the database:
```
make create_and_populate_db
```

### Running the app
```
make backend_up
make frontend_up
```

### Deploying the app
```
make back
make frontend_build
```

### Testing the app
```
backend_tests
```
