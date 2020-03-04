'''
Tests error endpoints
'''
from flask.json import loads

def test_bad_request_400(test_client):
    '''
    Tests endpoint for 400 errors
    '''
    response = test_client.post('/json', json={"this":"that"})
    response_json = loads(response.data.decode('utf-8'))
    assert response.status_code == 400
    assert all([value in ['error', 'format'] for value in response_json])

def test_unknown_404(test_client):
    '''
    Tests endpoint for 404 errors
    '''
    response = test_client.get('/bad_url')
    assert response.status_code == 404
    assert b"404 Error Marker" in response.data

    response = test_client.get('/bad_url', data='{"this":"that"}', content_type="application/json")
    response_json = loads(response.data.decode('utf-8'))
    assert response.status_code == 404
    assert 'error' in response_json

def test_wrong_method_405(test_client):
    '''
    Tests endpoint for 405 errors
    '''
    response = test_client.post('/', content_type="application/json")
    response_json = loads(response.data.decode('utf-8'))
    assert response.status_code == 405
    assert 'error' in response_json

    response = test_client.get('/json', content_type="application/html")
    assert response.status_code == 405
    assert b"405 Error Marker" in response.data

def test_teapot_418(test_client):
    '''
    Tests endpoint for 418 errors
    '''
    response = test_client.post('/json', content_type="application/html")
    assert response.status_code == 418
    assert b"418 Error Marker" in response.data
