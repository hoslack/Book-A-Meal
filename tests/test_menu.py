import unittest
from app import app


class TestMenu(unittest.TestCase):
    """Test the class menu and related endpoints"""

    def setUp(self):
        """Set up reusable data"""
        self.app = app.test_client()
        self.app.testing = True
        self.menu = [{'name': 'ugali', 'price': 100}, {'name': 'rice', 'price': 150}]

    def test_get_menu(self):
        result = self.app.get('/api/v1/menu/')
        self.assertEqual(result.status_code, 200)

    def test_get_all_menu_has_json(self):
        result = self.app.get('/api/v1/menu/')
        self.assertEqual(result.content_type, 'application/json')

    def test_menu_is_list(self):
        result = self.app.get('/api/v1/menu/')
        self.assertIsInstance(result.data, list)

    def test_add_menu_status_code(self):
        result = self.app.post('/api/v1/menu/', data=self.menu)
        self.assertEqual(result.status_code, 201)

    def test_add_menu_success_response(self):
        result = self.app.post('/api/v1/menu/', data=self.menu)
        self.assertIn(b'Success', result.data)

    def test_add_menu_without_data(self):
        result = self.app.post('/api/v1/menu/')
        self.assertNotEqual(result.status_code, 201)

    def test_duplicate_menu_creation(self):
        self.app.post('api/v1/menu/', self.menu)
        result = self.app.post('/api/v1/menu/', self.menu)
        self.assertEqual(result.status_code, 409)

    def test_edit_meal_status_code(self):
        result = self.app.put('/api/v1/meals/<int:id>/', data={'name': 'rice', 'price': 250})
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
