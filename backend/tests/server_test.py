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
    with app.app_context():
        egg_salad = Recipe(
            title='Yummy Salad Recipe',
            description='It has eggs')
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

# tests for filters
def assert_sorted(list_: List, key: str, reverse: bool):
    sorted_list = sorted(list_, key=lambda x: x[key], reverse=reverse)
    assert sorted_list == list_


def test_filter_by_review_count(app, client):
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

        # recipes = db.session.query(Recipe).all()
        # print(recipes)
        db.session.query(Recipe).all()

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


def test_filter_by_rating(app, client):
    # Given: More than one recipe with different ratings
    with app.app_context():
        egg_recipe1 = Recipe(
            title='Egg Salad',
            description='Eggcellent!',
            rating=2,
            ingredients=[Ingredient(name='1 teaspoon of brown sugar')],
            review_count=3
        )
        egg_recipe2 = Recipe(
            title='Egg Summer Salad',
            description='Egg-licious!',
            rating=1,
            ingredients=[Ingredient(name='2 teaspoons of brown sugar')],
            review_count=100
        )
        db.session.add(egg_recipe1)
        db.session.add(egg_recipe2)
        db.session.commit()

        # recipes = db.session.query(Recipe).all()
        # print(recipes)
        db.session.query(Recipe).all()

    # When: We filter the recipe results by "Highest" rating
    response = client.get('/search?q=egg&rating=DESC')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back the results in descending order,
    # with the highest-rated recipe displayed first
    data = response.get_json()
    # print(data)
    assert data['total'] == 2

    assert_sorted(data['data'], 'rating', True)

    # When: We filter the recipe results by "Lowest" rating
    response = client.get('/search?q=egg&rating=ASC')
    assert response.status_code == HTTPStatus.OK

    # Then We should get the back the results in ascending order,
    # with the lowest-rated recipe displayed first
    data = response.get_json()
    assert data['total'] == 2

    assert_sorted(data['data'], 'rating', False)


def test_filter_by_time(app, client):
    # Given: More than one recipe with different cooking times
    with app.app_context():
        egg_recipe1 = Recipe(
            title='Egg 1',
            time=15
        )
        egg_recipe2 = Recipe(
            title='Egg 2',
            time=31
        )
        egg_recipe3 = Recipe(
            title='Egg 3',
            time=60
        )
        egg_recipe4 = Recipe(
            title='Egg 4',
            time=75
        )
        db.session.add(egg_recipe1)
        db.session.add(egg_recipe2)
        db.session.add(egg_recipe3)
        db.session.add(egg_recipe4)
        db.session.commit()

        # recipes = db.session.query(Recipe).all()
        # print(recipes)
        db.session.query(Recipe).all()

    # When: We filter the recipe results by "< 15" option
    response = client.get('/search?q=egg&minTime=0&maxTime=15')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back only recipes with under 16 mins cooking time
    data = response.get_json()
    assert data['total'] == 1

    # When: We filter by "< 30"
    response = client.get('/search?q=egg&minTime=0&maxTime=30')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back only recipes with under 31 mins cooking time
    data = response.get_json()
    assert data['total'] == 1

    # When: We filter by "< 60"
    response = client.get('/search?q=egg&minTime=0&maxTime=60')
    assert response.status_code == HTTPStatus.OK

    # Then We should get back only recipes with 1 hour or less cooking time
    data = response.get_json()
    assert data['total'] == 3
