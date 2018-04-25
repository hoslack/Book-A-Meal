import unittest
from flask import json
from app import app


class TestMenu(unittest.TestCase):
    """Test the class menu and related endpoints"""

    def setUp(self):
        """Set up reusable data"""
        self.app = app.test_client()
        self.app.testing = True
        self.menu = [{'name': 'ugali', 'price': 100}, {'name': 'rice', 'price': 150}]

    def test_get_menu(self):
        rv = self.app.get('/api/v1/menu/')
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)

    def test_get_all_menu_has_json(self):
        rv = self.app.get('/api/v1/menu/')
        result = json.loads(rv.data.decode())
        self.assertEqual(result.content_type, 'application/json')

    def test_menu_is_list(self):
        rv = self.app.get('/api/v1/menu/')
        result = json.loads(rv.data.decode())
        self.assertIsInstance(result.data, list)

    def test_add_menu_status_code(self):
        rv = self.app.post('/api/v1/menu/', data=self.menu)
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 201)

    def test_add_menu_success_response(self):
        rv = self.app.post('/api/v1/menu/', data=self.menu)
        result = json.loads(rv.data.decode())
        self.assertIn(b'Success', result.data)

    def test_add_menu_without_data(self):
        rv = self.app.post('/api/v1/menu/')
        result = json.loads(rv.data.decode())
        self.assertNotEqual(result.status_code, 201)

    def test_duplicate_menu_creation(self):
        self.app.post('api/v1/menu/', self.menu)
        rv = self.app.post('/api/v1/menu/', self.menu)
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 409)

    def test_edit_meal_status_code(self):
        rv = self.app.put('/api/v1/meals/<int:id>/', data={'name': 'rice', 'price': 250})
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
