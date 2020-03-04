from flask.json import loads, dumps

def test_home(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"This API checks a Sudoku board to determine" in response.data
    assert b"Please format your JSON request" in response.data

def test_json_enpoint(test_client):
    pass_data = ["912468753","867135492","435279168","784952631","629317845","153684279","598726314","346891527","271543986"]
    fail_inner = [912468753,"867135492","435279168","784952631","629317845","153684279","598726314","346891527","271543986"]
    fail_outer = {"board":["912468753","867135492","435279168","784952631","629317845","153684279","598726314","346891527","271543986"]}
    response = test_client.post(
        '/json',
        json=pass_data,
        content_type='application/json')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == '{"result":"True"}\n'

    response = test_client.post(
        '/json',
        json=fail_inner,
        content_type='application/json')
    assert response.status_code == 400

    response = test_client.post(
        '/json',
        json=fail_outer,
        content_type='application/json')
    assert response.status_code == 400

    response = test_client.post(
        '/json',
        data={"hello":"there"},
        content_type='application/html')
    assert response.status_code == 418
