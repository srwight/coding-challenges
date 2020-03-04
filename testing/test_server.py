'''
Tests the create_app function
'''

from flask import Flask
from server import create_app

def test_create_app():
    '''
    Tests to be sure the create_app function is doing its job
    '''
    app = create_app('../testing/flask_test.cfg')
    assert app.testing
    assert 'sb' in app.blueprints
    assert isinstance(app, Flask)
