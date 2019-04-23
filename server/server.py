from flask import Flask, send_from_directory, request, jsonify
from sqlite_helper import search_by_ingredients
import os, sqlite3
import pickle

INGREDIENT_INDEX = None

app = Flask(__name__, static_url_path='/Users/hoeunsim2/Dropbox/dev/recipe-recommender')


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
    return send_from_directory('../images', path)


@app.route("/search")
def search():
    """
    Get parameters from the URL and display it.

    :return: the user's query (i.e., ingredients)
    """
    connection = sqlite3.connect('data.db')

    q = request.args.get('q', default=None, type=str).lower()

    minTime = request.args.get('minTime', default=None, type=int)
    maxTime = request.args.get('maxTime', default=None, type=int)

    rating = request.args.get('rating', default=None, type=int)

    review_count = request.args.get('review_count', default=None, type=int)

    if not q:
        abort(422, "Missing query")

    recipes = search_by_ingredients(connection, q.split(","),
                                    ingredient_index=INGREDIENT_INDEX)

    if minTime is not None and maxTime is not None:
        print(f"Using {minTime} - {maxTime} minute range.")
        recipes = list(filter(lambda recipe: recipe['time'] >= minTime and recipe['time'] <= maxTime, recipes))


    if review_count is not None:
        print(f"Sorting by {review_count}")
        recipes = sorted(recipes, key=lambda recipe: recipe['review_count'], reverse=review_count == 1)

    if rating is not None:
        print(f"Sorting by {rating}")
        recipes = sorted(recipes, key=lambda recipe: recipe['rating'], reverse=rating == 1)


    return jsonify({'total': len(recipes),'data': recipes[0:50]})


if __name__ == "__main__":
    with open('ingredient_index.pickle', 'rb') as index_file:
        INGREDIENT_INDEX = pickle.load(index_file)

        #print(INGREDIENT_INDEX)
    import logging
    logging.basicConfig(filename='access.log',level=logging.DEBUG)

    app.run(host='0.0.0.0', port=5000, threaded=True)
