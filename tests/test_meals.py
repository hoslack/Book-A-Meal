import unittest
from flask import json
from app import app


class TestMeals(unittest.TestCase):
    """Test the class meals and related endpoints"""

    def setUp(self):
        """Set up reusable data"""
        self.app = app.test_client()
        self.app.testing = True
        self.meal = {'name': 'ugali', 'price': 100}

    def test_get_all_meals_status_code(self):
        rv = self.app.get('/api/v1/meals/')
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)

    def test_get_all_meals_has_json(self):
        rv = self.app.get('/api/v1/meals/')
        result = json.loads(rv.data.decode())
        self.assertEqual(result.content_type, 'application/json')

    def test_add_meal_status_code(self):
        rv = self.app.post('/api/v1/meals/', data=self.meal)
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 201)

    def test_add_meal_success_response(self):
        rv = self.app.post('/api/v1/meals/', data=self.meal)
        result = json.loads(rv.data.decode())
        self.assertIn('Success', result)

    def test_add_meal_without_data(self):
        rv = self.app.post('/api/v1/meals/')
        result = json.loads(rv.data.decode())
        self.assertNotEqual(result.status_code, 201)

    def test_duplicate_meal_creation(self):
        self.app.post('/api/v1/meals', self.meal)
        rv = self.app.post('/api/v1/meals/', self.meal)
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 409)

    def test_edit_meal_status_code(self):
        rv = self.app.put('/api/v1/meals/<int:id>/', data={'name': 'rice', 'price': 250})
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)

    def test_delete_non_existent_meal(self):
        """Test for deleting of an id that does not exist"""
        rv = self.app.delete('/api/v1/-234/')
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()
