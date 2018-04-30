
import pytest
import json
import app

# Used pytest here to easily manage my session since some of the routes require login


@pytest.fixture
def client():
    """Create an instance of the application for sending requests"""
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client


def test_get_meals_success(client):
    """Test if admin can get all meals"""
    rv = client.get('/api/v1/meals/')
    assert rv.status_code == 200


def test_add_meal_success(client):
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "rice", "price": 120}))
    assert rv.status_code == 200


def test_add_meal_without_data(client):
    """Test if admin can add meal without data"""
    rv = client.post('/api/v1/meals/')
    assert rv.status_code == 400


def test_delete_non_existent_meal(client):
    """Test in case admin deletes non-existent meal"""
    rv = client.delete('/api/v1/meals/-432/')
    assert rv.status_code == 404


def test_delete_meal_success(client):
    """Test if meal can be deleted successfully"""
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "kuku", "price": 250}))  # create a meal
    json_data = json.loads(rv.data)
    meal_id = json_data['id']
    res = client.delete('/api/v1/meals/{}/'.format(meal_id))
    assert res.status_code == 200


def test_edit_non_existent_meal(client):
    """Test for editing a meal that does not exist"""
    rv = client.put('/api/v1/meals/-432/', data=json.dumps({"name": "fish fry", "price": 250}))
    assert rv.status_code == 404


def test_edit_meal_success(client):
    """Test if meal can be edited"""
    rv = client.post('/api/v1/meals/', data=json.dumps({"name": "chicken", "price": 250}))  # create a meal
    json_data = json.loads(rv.data)
    meal_id = json_data['id']
    res = client.put('/api/v1/meals/{}/'.format(meal_id), data=json.dumps({"name": "chicken masala", "price": 250}))
    assert res.status_code == 200




