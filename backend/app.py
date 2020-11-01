import os

from flask import Flask
from flask_cors import CORS

from backend.extensions import db
from backend.server import register_endpoints


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app(config=Config()):
    this_folder = os.path.dirname(os.path.realpath(__file__))
    app = Flask(__name__, static_url_path=os.path.abspath(os.path.join(this_folder, '../data/allrecipes')))
    CORS(app)

    app.config.from_object(config)

    db.init_app(app)

    # Register endpoints
    register_endpoints(app)

    return app
