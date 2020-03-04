from server import create_app
from flask import Flask

def test_create_app():
    app = create_app('../testing/flask_test.cfg')
    assert app.testing
    assert 'sb' in app.blueprints
    assert type(app) == Flask
