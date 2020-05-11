# Create an instance of Flask class and call it app
import os

from flask import Flask
from flask_cors import CORS

this_folder = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_url_path=os.path.abspath(os.path.join(this_folder, '../data/allrecipes')))
CORS(app)