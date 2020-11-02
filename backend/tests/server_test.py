from http import HTTPStatus
from typing import List

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


def assert_sorted(list_:List, key:str, reverse:bool):
    sorted_list = sorted(list_, key=lambda x: x[key], reverse=reverse)
    assert sorted_list == list_


# TODO: tests for filters
def test_search_by_review_count(app, client):
    # Given: More than one egg recipe with different
    # review counts
    with app.app_context():
        egg_recipe1 = Recipe(
            title='Egg Salad',
            description='Eggcellent!',
            ingredients=[Ingredient(name='1 teaspoon of brown sugar')],
            review_count=3
        )
        egg_recipe2 = Recipe(
            title='Egg Summer Salad',
            description='Egg-licious!',
            ingredients=[Ingredient(name='2 teaspoons of brown sugar')],
            review_count=100
        )
        db.session.add(egg_recipe1)
        db.session.add(egg_recipe2)
        db.session.commit()

        recipes = db.session.query(Recipe).all()
        print(recipes)

    # When: When we filter egg results by "Highest" reviews
    response = client.get('/search?q=egg&review=DESC')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get the results in descending order, with
    # the most reviewed recipe displayed first
    data = response.get_json()
    assert data['total'] == 2

    assert_sorted(data['data'], 'review_count', True)

    # When: When we filter egg results by "Lowest" reviews
    response = client.get('/search?q=egg&review=ASC')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get the results in ascending order, with
    # the lowest reviewed recipe displayed first
    data = response.get_json()
    assert data['total'] == 2

    assert_sorted(data['data'], 'review_count', False)

