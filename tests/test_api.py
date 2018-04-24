import unittest
from app import app


class TestBookAMealAPI(unittest.TestCase):
    """Class for testing all the API endpoints"""
    def setUp(self):
        """Initializing a test client and making the environment a testing one"""
        self.app = app.test_client()
        self.app.testing = True
        self.meal = {'name': 'ugali', 'price': 100}

    def sign_in(self, email='user@gmail.com', password='testpass'):
        user_data = {
            'email': email,
            'password': password
        }
        return self.app.post('/auth/signup', data=user_data)

    def log_in(self, email='user@gmail.com', password='testpass'):
        user_data = {
            'email': email,
            'password': password
        }
        return self.app.post('/auth/login', data=user_data)

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_signin_status_code(self):
        result = self.sign_in()
        self.assertEqual(result.status_code, 200)

    def test_login_correct_login(self):
        """test login after signing in"""
        self.sign_in()
        result = self.log_in()
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Success', result.data)

    def test_login_with_wrong_credentials(self):
        """test successful login"""
        self.sign_in()  # must sign in first for successful login
        result = self.log_in(email='wrong@mail', password='wrongpass')
        self.assertIn(b'Wrong Credentials, try again', result.data)

    def test_get_all_meals_status_code(self):
        result = self.app.get('/meals')
        self.assertEqual(result.status_code, 200)

    def test_get_all_meals_has_json(self):
        result = self.app.get('/meals')
        self.assertEqual(result.content_type, 'application/json')

    def test_add_meal_status_code(self):
        result = self.app.post('/meals', data=self.meal)
        self.assertEqual(result.status_code, 201)

    def test_add_meal_success_response(self):
        result = self.app.post('/meals', data=self.meal)
        self.assertIn('Success', result)

    def test_add_meal_without_data(self):
        result = self.app.post('/meals')
        self.assertNotEqual(result.status_code, 201)

    def test_duplicate_meal_creation(self):
        self.app.post('/meals', self.meal)
        result1 = self.app.post('/meals', self.meal)
        self.assertEqual(result1.status_code, 409)

    def test_edit_meal_status_code(self):
        result = self.app.put('/meals/1', data={'name': 'rice', 'price': 250})
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
