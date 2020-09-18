import os

from flask import Flask
from flask_cors import CORS

from backend.extensions import db


def create_app():
    this_folder = os.path.dirname(os.path.realpath(__file__))
    app = Flask(__name__, static_url_path=os.path.abspath(os.path.join(this_folder, '../data/allrecipes')))
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app

app = create_app()