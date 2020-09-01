from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from backend.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)
    review = db.Column(db.Integer)
    time = db.Column(db.Integer)
    image = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.String)

    steps = db.relationship('RecipeStep', back_populates='recipe')
    ingredients = db.relationship('Ingredient',
                                  secondary='recipe_ingredients')

    def __init__(self, title, rating, review, time, image, url, description, steps, ingredients):
        self.title = title
        self.rating = rating
        self.review = review
        self.time = time
        self.image = image
        self.url = url
        self.description = description
        self.steps = steps
        self.ingredients = ingredients


class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredients'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
    quantity = db.Column(db.String)
    value = db.Column(db.Float)
    unit = db.Column(db.String)
    entity = db.Column(db.String)
    quant_mL = db.Column(db.Float)


class RecipeStep(db.Model):
    __tablename__ = 'recipe_steps'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    step_num = db.Column(db.Integer, primary_key=True)
    instruction = db.Column(db.String, nullable=False)

    recipe = db.relationship('Recipe', back_populates='steps')
