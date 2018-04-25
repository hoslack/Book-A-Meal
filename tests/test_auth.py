import unittest
from flask import json, jsonify
from app import app


class TestAuth(unittest.TestCase):
    """Class for testing all the API endpoints"""
    def setUp(self):
        """Initializing a test client and making the environment a testing one"""
        self.app = app.test_client()
        self.app.testing = True

    def sign_in(self, email='user@gmail.com', password='testpass'):
        user_data = jsonify(email=email, password=password)
        return self.app.post('/api/v1/auth/signup/', data=user_data)

    def log_in(self, email='user@gmail.com', password='testpass'):
        user_data = jsonify(email=email, password=password)
        return self.app.post('/api/v1/auth/login/', data=user_data)

    def test_home_status_code(self):

        rv = self.app.get('/api/v1/')  # rv is return value
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)

    def test_signin_status_code(self):
        rv = self.sign_in()
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)

    def test_login_correct_login(self):
        """test login after signing in"""
        self.sign_in()
        rv = self.log_in()
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Success', result.data)

    def test_login_with_wrong_credentials(self):
        """test successful login"""
        self.sign_in()  # must sign in first for successful login
        rv = self.log_in(email='wrong@mail', password='wrongpass')
        result = json.loads(rv.data.decode())
        self.assertIn(b'Wrong Credentials, try again', result.data)


if __name__ == "__main__":
    unittest.main()
