from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from backend.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)


class Recipe(db.Model):
    __tablename__ = 'Recipe'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)
    review = db.Column(db.Integer)
    time = db.Column(db.Integer)
    image = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.String)

    steps = db.relationship('RecipeStep', back_populates='recipe')

class Ingredient(db.Model):
    __tablename__ = 'Ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class RecipeIngredient(db.Model):
    __tablename__ = 'RecipeIngredient'
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('Ingredient.id'), primary_key=True)
    quantity = db.Column(db.String)
    value = db.Column(db.Float)
    unit = db.Column(db.String)
    entity = db.Column(db.String)
    quant_mL = db.Column(db.Float)

class RecipeStep(db.Model):
    __tablename__ = 'RecipeStep'
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'), primary_key=True)
    step_num = db.Column(db.Integer, primary_key=True)
    instruction = db.Column(db.String, nullable=False)

    recipe = db.relationship('Recipe', back_populates='steps')


# db.create_all()
