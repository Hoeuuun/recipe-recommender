from http import HTTPStatus

import pytest

from backend.extensions import db
from backend.model import Recipe


def test_search_in_recipe_title(app, client):
    # Given: An egg salad exists in the database with egg in title.
    with app.app_context():
        egg_salad = Recipe(title='Egg salady poo')
        db.session.add(egg_salad)
        db.session.commit()

    # When: We search for egg.
    response = client.get('/search?q=egg')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back 1 result.
    data = response.get_json()
    assert data['total'] == 1


def test_search_in_recipe_description(app, client):
    # Given: An egg salad exists in the database with egg in
    # description but not title.
    with app.app_context():
        egg_salad = Recipe(
            title='Hello, I am a recipe',
            description='There are eggs here')
        db.session.add(egg_salad)
        db.session.commit()
    # When: We search for egg.
    response = client.get('/search?q=egg')
    assert response.status_code == HTTPStatus.OK

    # Then: We should get back 1 result.
    data = response.get_json()
    assert data['total'] == 1
