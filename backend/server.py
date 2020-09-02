import logging
import os
import pickle
import sqlite3

from flask import send_from_directory, request, jsonify, abort

from sqlalchemy import and_, desc, asc, or_

from backend.model import db, Recipe, RecipeIngredient, Ingredient, RecipeStep
from backend.sqlite_helper import search_by_ingredients

from backend.app import app

_logger = logging.getLogger(__name__)

INGREDIENT_INDEX = None


# The default page
@app.route("/")
def index():
    print(os.path.dirname(os.path.realpath(__file__)))
    with open('../static/index.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route("/<path:path>")
def send_static(path):
    """
    Serve static content by default.
    """
    print(os.path.dirname(os.path.realpath(__file__)))
    return send_from_directory('../static', path)


@app.route('/data/allrecipes/images/userphotos/<path:path>')
def send_photos(path):
    return send_from_directory('../data/allrecipes/images/userphotos', path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('../data/allrecipes/images', path)


@app.route("/search")
def search():
    connection = sqlite3.connect('data.db')

    q = request.args.get('q', default=None, type=str)

    if not q:
        abort(422, "Missing query")  # 422 unprocessable entity

    q = q.lower()

    minTime = request.args.get('minTime', default=None, type=int)
    maxTime = request.args.get('maxTime', default=None, type=int)

    rating = request.args.get('rating', default=None, type=str)

    review_count = request.args.get('review', default=None, type=str)

    ilike_query = '%'.join(q.split(','))
    ilike_query = f'%{ilike_query}%'
    recipes_query = db.session.query(Recipe).filter(
        or_(
            Recipe.description.ilike(ilike_query),
            Recipe.title.ilike(ilike_query),
            Recipe.ingredients.any(Ingredient.name.ilike(ilike_query)),
            # Recipe.steps.any(RecipeStep.instruction.ilike(ilike_query))
        ))

    if minTime is not None and maxTime is not None:
        recipes_query = recipes_query.filter(and_(
            Recipe.time >= minTime,
            Recipe.time <= maxTime
        ))
    if review_count is not None:
        fn = desc if review_count == 'DESC' else asc
        recipes_query = recipes_query.order_by(fn(Recipe.review_count))
    if rating is not None:
        fn = desc if rating == 'DESC' else asc
        recipes_query = recipes_query.order_by(fn(Recipe.rating))

    recipes_query = recipes_query.limit(50)

    recipes = recipes_query.all()



    """
    recipes = search_by_ingredients(connection, q.split(","),
                                    ingredient_index=INGREDIENT_INDEX)

    if minTime is not None and maxTime is not None:
        print(f"Using {minTime} - {maxTime} minute range.")
        recipes = list(filter(lambda recipe: recipe['time'] >= minTime and recipe['time'] <= maxTime, recipes))

    if review_count is not None:
        print(f"Sorting by {review_count}")
        recipes = sorted(recipes, key=lambda recipe: recipe['review_count'], reverse=review_count == 'DESC')

    if rating is not None:
        print(f"Sorting by {rating}")
        recipes = sorted(recipes, key=lambda recipe: recipe['rating'], reverse=rating == 'DESC')
    """

    return jsonify({'total': len(recipes), 'data': [recipe.to_dict() for recipe in recipes]})


if __name__ == "__main__":
    with open('ingredient_index.pickle', 'rb') as index_file:
        INGREDIENT_INDEX = pickle.load(index_file)

    app.run(host='0.0.0.0', port=5000, threaded=True)
