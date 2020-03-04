'''
pytest configuration file; contains fixtures for testing
Adapted from a tutorial
'''

import pytest
from server import create_app

@pytest.fixture(scope='module')
def test_client():
    '''
    Builds a test client for use during testing
    '''
    flask_app = create_app('../testing/flask_test.cfg')

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
