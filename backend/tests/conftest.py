import os

import pytest

from backend.app import create_app, Config
from backend.extensions import db


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///test_data_{os.getpid()}.db'


@pytest.fixture
def app():
    app = create_app(TestConfig())
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
