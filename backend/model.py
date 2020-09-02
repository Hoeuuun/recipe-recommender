from typing import Dict

from flask_sqlalchemy import SQLAlchemy

from backend.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Recipe(db.Model):
    __tablename__ = 'Recipe'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)
    review_count = db.Column(db.Integer)
    time = db.Column(db.Integer)
    image = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.String)

    steps = db.relationship('RecipeStep', back_populates='recipe')
    ingredients = db.relationship('Ingredient',
                                  secondary='RecipeIngredients')

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

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'rating': self.rating,
            'review_count': self.review_count,
            'time': self.time,
            'image': self.image,
            'description': self.description,
            'ingredients': [ingredient.name for ingredient in self.ingredients],
            'directions': [step.instruction for step in self.steps],
        }


class Ingredient(db.Model):
    __tablename__ = 'Ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name
        }


class RecipeIngredient(db.Model):
    __tablename__ = 'RecipeIngredients'

    recipeId = db.Column(db.Integer, db.ForeignKey('Recipe.id'), primary_key=True)
    ingredientId = db.Column(db.Integer, db.ForeignKey('Ingredient.id'), primary_key=True)
    quantity = db.Column(db.String)
    value = db.Column(db.Float)
    unit = db.Column(db.String)
    entity = db.Column(db.String)
    quant_mL = db.Column(db.Float)


class RecipeStep(db.Model):
    __tablename__ = 'RecipeSteps'

    recipeId = db.Column(db.Integer, db.ForeignKey('Recipe.id'), primary_key=True)
    stepNumber = db.Column(db.Integer, primary_key=True)
    instruction = db.Column(db.String, nullable=False)

    recipe = db.relationship('Recipe', back_populates='steps')

    def to_dict(self) -> Dict:
        return {
            'stepNumber': self.stepNumber,
            'instruction': self.instruction,
        }
