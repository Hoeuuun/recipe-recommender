# recipe-recommender
* [Recipe-Recommender](https://hoeunsim.com/rr/) is a search engine with 91k+ recipes from [Allrecipes](https://www.allrecipes.com/).
* It’s a web app for finding recipes and discovering new cuisines, dishes, and drinks!
* Users may quickly search for recipes by entering into the search box keywords, like recipe names or ingredients or both.
* Results are displayed as cards in a Pinterest-like grid. 
* Clicking on a recipe card will launch that recipe’s popup window, that contains more information about the recipe, including a list of required ingredients and cooking instructions.
* Optionally, users may sort recipe results by rating, time, or reviews.
* TL;DR: Recipe-Recommender helps you get cooking, bringing out your inner chef!


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
make backend_tests
```
