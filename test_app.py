from app import db, helper_function


# unit test
def test_helper_function():
    result = helper_function(2,2)
    assert result == 4



# api test
def test_ping_endpoint(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json.get('status') == 'ok'


# integration test
def test_add_endpoint(client):
    response = client.post('/add', json={'username': 'abc'})
    assert response.status_code == 200
    assert 'abc' in db



