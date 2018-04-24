import unittest
from app import app


class TestBookAMealAPI(unittest.TestCase):
    """Class for testing all the API endpoints"""
    def setUp(self):
        """Initializing a test client and making the environment a testing one"""
        self.app = app.test_client()
        self.app.testing = True

    def sign_in(self, email='user@gmail.com', password='testpass'):
        user_data = {
            'email': email,
            'password': password
        }
        return self.app.post('/api/v1/auth/signup', data=user_data)

    def log_in(self, email='user@gmail.com', password='testpass'):
        user_data = {
            'email': email,
            'password': password
        }
        return self.app.post('/api/v1/auth/login', data=user_data)

    def test_home_status_code(self):
        result = self.app.get('/api/v1/')
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


if __name__ == "__main__":
    unittest.main()