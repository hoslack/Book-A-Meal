import unittest
from app import app


class TestOrders(unittest.TestCase):
    """Test the class orders and related endpoints"""

    def setUp(self):
        """Set up reusable data"""
        self.app = app.test_client()
        self.app.testing = True
        self.order = {'cutomer': 'hoslack', 'name': 'ugali', 'price': 100}

    def test_get_order(self):
        result = self.app.get('/api/v1/orders')
        self.assertEqual(result.status_code, 200)

    def test_get_all_orders_has_json(self):
        result = self.app.get('/api/v1/orders')
        self.assertEqual(result.content_type, 'application/json')

    def test_orders_is_dict(self):
        result = self.app.get('/api/v1/orders')
        self.assertIsInstance(result.data, dict)

    def test_add_order_status_code(self):
        result = self.app.post('/api/v1/orders', data=self.order)
        self.assertEqual(result.status_code, 201)

    def test_add_order_success_response(self):
        result = self.app.post('/api/v1/orders', data=self.order)
        self.assertIn(b'Success', result.data)

    def test_add_order_without_data(self):
        result = self.app.post('/api/v1/orders')
        self.assertNotEqual(result.status_code, 201)

    def test_edit_order_status_code(self):
        result = self.app.put('/api/v1/orders/<int:id>', data={'customer': 'hos', 'name': 'rice', 'price': 250})
        self.assertEqual(result.status_code, 200)

    def test_edit_non_existent_order(self):
        result = self.app.put('/api/v1/orders/-134', data={'customer': 'hos', 'name': 'rice', 'price': 250})
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()
