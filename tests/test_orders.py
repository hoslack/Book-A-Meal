
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


def test_get_orders_success(client):
    """Test if admin can get all orders"""
    rv = client.get('/api/v1/orders/')
    assert rv.status_code == 200


def test_create_order_success(client):
    rv = client.post('/api/v1/orders/', data=json.dumps({"customer_name": "hoslack", "meal1": "ugali", "meal2": "beef", "total_price": 120}))
    assert rv.status_code == 200


def test_create_order_without_data(client):
    """Test if customer can create order without data"""
    rv = client.post('/api/v1/orders/')
    assert rv.status_code == 400


def test_edit_non_existent_order(client):
    """Test for editing an order that does not exist"""
    rv = client.put('/api/v1/orders/-432/', data=json.dumps({"customer_name": "hoslack", "meal1": "biryani", "meal2":"beef",
                                                             "total_price": 120}))
    assert rv.status_code == 404


def test_edit_order_success(client):
    """Test if meal can be edited"""
    rv = client.post('/api/v1/orders/', data=json.dumps({"customer_name": "hoslack", "meal1": "biryani", "meal2": "beef",                                                  "total_price": 120}))  # create a meal
    json_data = json.loads(rv.data)
    meal_id = json_data['id']
    res = client.put('/api/v1/orders/{}/'.format(meal_id), data=json.dumps({"customer_name": "hoslack", "meal1": "tender goat",
                                                                           "meal2": "beef", "total_price": 120}))
    assert res.status_code == 200


