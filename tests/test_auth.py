import unittest
from flask import json
from app import app


class TestAuth(unittest.TestCase):
    """Class for testing all the API endpoints"""
    def setUp(self):
        """Initializing a test client and making the environment a testing one"""
        self.app = app.test_client(self)
        app.config.testing = True
        self.user_data = json.dumps({"name": "hoslack", "email": "hos", "password": "hos"})
        self.login_data = json.dumps({"email": "hos", "password": "hos"})

    def test_home_status_code(self):
        result = self.app.get('/api/v1/')
        self.assertEqual(result.status_code, 200)

    def test_correct_signup(self):
        result = self.app.post('/api/v1/auth/signup/', data=self.user_data)
        self.assertEqual(result.status_code, 201)
        data = json.loads(result.data)
        self.assertEqual(data["message"], "User registration successful")

    def test_signup_without_credentials(self):
        result = self.app.post('/api/v1/auth/signup/', data=json.dumps({}))
        self.assertEqual(result.status_code, 400)

    def test_signup_with_same_email(self):
        self.app.post('/api/v1/auth/signup/', data=self.user_data)
        result = self.app.post('/api/v1/auth/signup/', data=self.user_data)
        self.assertEqual(result.status_code, 409)
        data = json.loads(result.data)
        self.assertEqual(data["message"], "User exists, log in instead")

    def test_correct_login(self):
        self.app.post('/api/v1/auth/signup/', data=json.dumps({"name": "hoslack", "email": "hos@hos", "password": "hos"}))
        result = self.app.post('/api/v1/auth/login/', data=json.dumps({"email": "hos@hos", "password": "hos"}))
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.data)
        self.assertEqual(data["message"], "Login successful")

    def test_login_non_registered_user(self):
        self.app.post('/api/v1/auth/signup/', data=json.dumps({"name": "hoslack", "email": "hos@hos", "password": "hos"}))
        result = self.app.post('/api/v1/auth/login/', data=json.dumps({"email": "hoslack", "password": "hos"}))
        self.assertEqual(result.status_code, 401)
        data = json.loads(result.data)
        self.assertEqual(data["message"], "You are not a registered user. Please register")

    def test_login_with_wrong_credentials(self):
        self.app.post('/api/v1/auth/signup/', data=json.dumps({"name": "ochieng", "email": "ochi", "password": "ochi"}))
        result = self.app.post('/api/v1/auth/login/', data=json.dumps({"email": "ochi", "password": "hrk"}))
        self.assertEqual(result.status_code, 401)
        data = json.loads(result.data)
        self.assertEqual(data["message"], "Wrong Email or Password")

    def test_login_without_credentials(self):
        self.app.post('/api/v1/auth/signup/', data=json.dumps({"name": "hos1", "email": "hos1", "password": "hos1"}))
        result = self.app.post('/api/v1/auth/login/', data=json.dumps({}))
        self.assertEqual(result.status_code, 400)
        data = json.loads(result.data)
        self.assertEqual(data["message"], "Please enter your credentials")


if __name__ == "__main__":
    unittest.main()
