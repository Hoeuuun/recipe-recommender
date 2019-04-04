from flask import Flask, send_from_directory, request, jsonify
from recipesDriver import search_by_ingredients
import os, sqlite3

app = Flask(__name__, static_url_path='/Users/hoeunsim2/Dropbox/dev/recipe-recommender')


@app.route("/")
def index():
    print(os.path.dirname(os.path.realpath(__file__)))
    with open('../static/index.html', 'r') as file:
        return file.read()


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('../static/js', path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('../images', path)


@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('../fonts', path)


@app.route('/data/allrecipes/images/userphotos/<path:path>')
def send_photos(path):
    return send_from_directory('../data/allrecipes/images/userphotos', path)


@app.route("/search")
def search():
    """
    Get parameters from the URL and display it.

    :return: the user's query (i.e., ingredients)
    """
    connection = sqlite3.connect('../data.db')

    q = request.args.get('q', default=None, type=str)
    if not q:
        abort(422, "Missing query")

    recipes = search_by_ingredients(connection, q.split(","))
    print(recipes)

    return jsonify(recipes[0:9])


if __name__ == "__main__":
    app.run()
