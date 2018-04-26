import unittest
from app import app


class TestMeals(unittest.TestCase):
    """Test the class meals and related endpoints"""

    def setUp(self):
        """Set up reusable data"""
        self.app = app.test_client()
        self.app.testing = True
        self.meal = {'name': 'ugali', 'price': 100}

    def test_get_all_meals_status_code(self):
        result = self.app.get('/api/v1/meals/')
        self.assertEqual(result.status_code, 200)

    def test_get_all_meals_has_json(self):
        result = self.app.get('/api/v1/meals/')
        self.assertEqual(result.content_type, 'application/json')

    def test_add_meal_status_code(self):
        result = self.app.post('/api/v1/meals/', data=self.meal)
        self.assertEqual(result.status_code, 201)

    def test_add_meal_success_response(self):
        result = self.app.post('/api/v1/meals/', data=self.meal)
        self.assertIn('Success', result)

    def test_add_meal_without_data(self):
        result = self.app.post('/api/v1/meals/')
        self.assertNotEqual(result.status_code, 201)

    def test_duplicate_meal_creation(self):
        self.app.post('/api/v1/meals', self.meal)
        result = self.app.post('/api/v1/meals/', self.meal)
        self.assertEqual(result.status_code, 409)

    def test_edit_meal_status_code(self):
        result = self.app.put('/api/v1/meals/<int:id>/', data={'name': 'rice', 'price': 250})
        self.assertEqual(result.status_code, 200)

    def test_delete_non_existent_meal(self):
        """Test for deleting of an id that does not exist"""
        result = self.app.delete('/api/v1/-234/')
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()
