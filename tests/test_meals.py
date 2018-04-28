import unittest
from flask import jsonify
from app import app
from app.order.meal import Meal


class TestMeals(unittest.TestCase):
    """Test the class meals and related endpoints"""

    def setUp(self):
        """Set up reusable data"""
        self.app = app.test_client()
        self.app.testing = True
        self.meal_data = jsonify({'name': 'ugali', 'price': 100})
        self.meal = Meal(name='ugali', price=100)

    def test_meal_creation(self):
        """Test if meal object is an instance of Meal class"""
        with app.app_context():
            self.assertIsInstance(self.meal, Meal)

    def test_get_all_meals_status_code(self):
        with app.app_context():
            result = self.app.get('/api/v1/meals/')
            self.assertEqual(result.status_code, 200)

    def test_get_all_meals_has_json(self):
        with app.app_context():
            result = self.app.get('/api/v1/meals/')
            self.assertEqual(result.content_type, 'application/json')

    def test_add_meal_status_code(self):
        with app.app_context():
            result = self.app.post('/api/v1/meals/', form=self.meal_data)
            self.assertEqual(result.status_code, 201)

    def test_add_meal_success_response(self):
        with app.app_context():
            result = self.app.post('/api/v1/meals/', form=self.meal_data)
            self.assertIn('Success', result)

    def test_add_meal_without_data(self):
        with app.app_context():
            result = self.app.post('/api/v1/meals/')
            self.assertNotEqual(result.status_code, 201)

    def test_duplicate_meal_creation(self):
        with app.app_context():
            self.app.post('/api/v1/meals', self.meal_data)
            result = self.app.post('/api/v1/meals/', self.meal_data)
            self.assertEqual(result.status_code, 409)

    def test_edit_meal_status_code(self):
        with app.app_context():
            result = self.app.put('/api/v1/meals/<int:id>/', form=jsonify({'name': 'rice', 'price': 250}))
            self.assertEqual(result.status_code, 200)

    def test_delete_non_existent_meal(self):
        """Test for deleting of an id that does not exist"""
        with app.app_context():

            result = self.app.delete('/api/v1/-234/')
            self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()