from app import helper_function

# unit test
def test_helper_function():
    assert helper_function(2,2) == 4
    assert helper_function(0,0) == 0
    assert helper_function(-5, -4) == -9


# api test
def test_ping_endpoint(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json.get('status') == 'ok'


# integration test
def test_user_endpoint(client):
    response = client.post('/users', json={'username': 'abc', 'firstname': 'FIRSTNAME', 'lastname': 'LASTNAME'})
    assert response.status_code == 201

    response = client.get('/users/abc')
    user = response.json
    assert response.status_code == 200
    assert user['username'] == 'abc'



