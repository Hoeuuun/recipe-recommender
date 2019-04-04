from flask import Flask

app = Flask(__name__, static_url_path='/Users/hoeunsim2/Dropbox/dev/recipe-recommender')


@app.route("/")
def index():
    with open('index.html', 'r') as file:
        return file.read()
    #return app.send_static_file("index.html")

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('fonts', path)

@app.route('/data/allrecipes/images/userphotos/<path:path>')
def send_photos(path):
    return send_from_directory('data/allrecipes/images/userphotos', path)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/search")
def search():
    """
    Get parameters from the URL and display it.

    :return: the user's query (i.e., ingredients)
    """
    connection = sqlite3.connect('schema.db')

    q = request.args.get('q', default=None, type=str)
    if not q:
        abort(422, "Missing query")

    recipes = search_by_ingredients(connection, q.split(","))
    print(recipes)

    return jsonify(recipes[0:9])

    #   return f"<h1>{q}</h1>"


if __name__ == "__main__":
    app.run()
