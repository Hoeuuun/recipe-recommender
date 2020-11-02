from http import HTTPStatus

import pytest

from backend.extensions import db
from backend.model import Recipe, Ingredient


def test_search_in_recipe_title(app, client):
    # Given: An egg salad exists in the database with egg in title
    with app.app_context():
        egg_salad = Recipe(title='Yummy Egg Salad')
        db.session.add(egg_salad)
        db.session.commit()

    # When: We search for egg
    response = client.get('/search?q=egg')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back 1 result
    data = response.get_json()
    assert data['total'] == 1


def test_search_in_recipe_description(app, client):
    # Given: An egg salad exists in the database with egg in
    # description but not title
    with app.app_context():
        egg_salad = Recipe(
            title='Hello, I am a recipe',
            description='There are eggs here')
        db.session.add(egg_salad)
        db.session.commit()
    # When: We search for egg
    response = client.get('/search?q=egg')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back 1 result
    data = response.get_json()
    assert data['total'] == 1


def test_search_in_recipe_ingredients(app, client):
    # Given: An egg salad exists in the database with egg in
    # ingredients list but not in title nor description
    with app.app_context():
        egg_salad = Recipe(
            title='A Salad Recipe',
            description='It\'s delicious!',
            ingredients=[Ingredient(name='1 brown eggs.')]
        )
        db.session.add(egg_salad)
        db.session.commit()
    # When: we search egg
    response = client.get('/search?q=egg')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back 1 result
    data = response.get_json()
    assert data['total'] == 1


def test_search_no_results(app, client):
    # Given: A non-empty database with no recipes containing eggs
    with app.app_context():
        sugar_recipe = Recipe(
            title='A Sugary Recipe',
            description='It\'s sweet!',
            ingredients=[Ingredient(name='1 teaspoon of brown sugar')]
        )
        db.session.add(sugar_recipe)
        db.session.commit()

    # When: We search for egg
    response = client.get('/search?q=egg')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back 0 as the result
    data = response.get_json()
    assert data['total'] == 0

# TODO: tests for filters