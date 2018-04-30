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


def test_get_menu_success(client):
    """Test if customer can get all meals menu"""
    rv = client.get('/api/v1/menu/')
    assert rv.status_code == 200


def test_add_meal_to_menu_success(client):
    rv = client.post('/api/v1/menu/', data=json.dumps({"meal1": "rice", "meal2": "beef", "total_price": 120}))
    assert rv.status_code == 200


def test_add_meal_to_menu_without_data(client):
    """Test if admin can add meal without data"""
    rv = client.post('/api/v1/menu/')
    assert rv.status_code == 400







