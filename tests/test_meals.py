
import pytest
import json
import app


@pytest.fixture
def client():
    """Create a an instance of the application for sending requests"""
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client


def signup(client, name, email, password):
    """A method to signup the client every time there is a request"""
    return client.post('/api/v1/auth/signup/', data=json.dumps({"name": name, "email": email, "password": password}))


def login(client, email, password):
    """A method to login the client every time it makes a request"""
    return client.post('/api/v1/auth/login/', data=json.dumps({"email": email, "password": password}))


def test_get_meals_success(client):
    """Test if admin can get all meals"""
    login(client, 'admin@gmail.com', '1234')
    rv = client.get('/api/v1/meals/')
    assert rv.status_code == 200


def test_only_admin_can_get_meals(client):
    """Test if only the admin can get meals"""
    signup(client, 'hos', 'hos@gmail.com', '1234')
    login(client, 'hos@gmail.com', '1234')
    rv = client.get('/api/v1/meals/')
    assert rv.status_code == 401
    json_data = json.loads(rv.data)
    assert json_data['message'] == 'Please login as admin to perform the operation'


def test_add_meal_success(client):
    login(client, 'admin@gmail.com', '1234')
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "rice", "price": 120}))
    assert rv.status_code == 200


def test_only_admin_can_add_meals(client):
    """Test if only the admin can add meals"""
    signup(client, 'hos1', 'hos1@gmail.com', '1234')
    login(client, 'hos1@gmail.com', '1234')
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "kuskus", "price": 250}))
    assert rv.status_code == 401
    json_data = json.loads(rv.data)
    assert json_data['message'] == 'Please login as admin to perform the operation'


def test_add_meal_without_data(client):
    """Test if admin can add meal without data"""
    login(client, 'admin@gmail.com', '1234')
    rv = client.post('/api/v1/meals/')
    assert rv.status_code == 400


def test_delete_non_existent_meal(client):
    """Test in case admin deletes non-existent meal"""
    login(client, 'admin@gmail.com', '1234')
    rv = client.delete('/api/v1/meals/-432/')
    assert rv.status_code == 404


def test_delete_meal_success(client):
    """Test if meal can be deleted successfully"""
    login(client, 'admin@gmail.com', '1234')
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "kuku", "price": 250}))  # create a meal
    json_data = json.loads(rv.data)
    meal_id = json_data['id']
    res = client.delete('/api/v1/meals/{}/'.format(meal_id))
    assert res.status_code == 200


def test_only_admin_can_delete_meals(client):
    """Test if only the admin can add meals"""
    signup(client, 'hos1', 'hos1@gmail.com', '1234')
    login(client, 'admin@gmail.com', '1234')
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "fish", "price": 250}))
    json_data = json.loads(rv.data)
    meal_id = json_data['id']
    login(client, 'hos1@gmail.com', '1234')
    res = client.delete('/api/v1/meals/{}/'.format(meal_id))
    assert res.status_code == 401
    json_res = json.loads(res.data)
    assert json_res['message'] == 'Please login as admin to perform the operation'


def test_edit_non_existent_meal(client):
    """Test for editing a meal that does not exist"""
    login(client, 'admin@gmail.com', '1234')
    rv = client.put('/api/v1/meals/-432/', data=json.dumps({"name": "fish fry", "price": 250}))
    assert rv.status_code == 404


def test_edit_meal_success(client):
    """Test if meal can be edited"""
    login(client, 'admin@gmail.com', '1234')
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "chicken", "price": 250}))  # create a meal
    json_data = json.loads(rv.data)
    meal_id = json_data['id']
    res = client.put('/api/v1/meals/{}/'.format(meal_id), data=json.dumps({"name": "chicken masala", "price": 250}))
    assert res.status_code == 200


def test_only_admin_can_edit_meal(client):
    """Test only admin is allowed to edit meal"""
    signup(client, 'hos2', 'hos2@gmail.com', '1234')
    login(client, 'admin@gmail.com', '1234')
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "chicken tika", "price": 250}))  # create a meal
    json_data = json.loads(rv.data)
    meal_id = json_data['id']
    login(client, 'hos2@gmail.com', '1234')
    res = client.put('/api/v1/meals/{}/'.format(meal_id), data=json.dumps({"name": "chicken choma", "price": 250}))
    assert res.status_code == 401
