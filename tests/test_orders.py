import unittest
from flask import jsonify, json
from app import app
from app.order.order import Order


class TestOrders(unittest.TestCase):
    """Test the class orders and related endpoints"""

    def setUp(self):
        """Set up reusable data"""
        self.app = app.test_client()
        self.app.testing = True
        self.customer = 'hoslack'
        self.meal = jsonify(name='ugali', price=100)
        self.order = Order(customer_name=self.customer, meal=self.meal)

    def test_order_creation(self):
        self.assertIsInstance(self.order, Order, "An instance of order was not creaated")

    def test_get_order(self):
        rv = self.app.get('/api/v1/orders/')
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)

    def test_get_all_orders_has_json(self):
        rv = self.app.get('/api/v1/orders/')
        result = json.loads(rv.data.decode())
        self.assertEqual(result.content_type, 'application/json')

    def test_orders_is_dict(self):
        rv = self.app.get('/api/v1/orders/')
        result = json.loads(rv.data.decode())
        self.assertIsInstance(result.data, list)

    def test_add_order_status_code(self):
        rv = self.app.post('/api/v1/orders/', data=self.order)
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 201)

    def test_add_order_success_response(self):
        rv = self.app.post('/api/v1/orders/', data=self.order)
        result = json.loads(rv.data.decode())
        self.assertIn(b'Success', result.data)

    def test_add_order_without_data(self):
        rv = self.app.post('/api/v1/orders/')
        result = json.loads(rv.data.decode())
        self.assertNotEqual(result.status_code, 200)

    def test_edit_order_status_code(self):
        self.app.post('/api/v1/orders/', data=Order('hos', jsonify(name='rice', price=290)))
        rv = self.app.put('/api/v1/orders/<int:id>/', data=Order('hos', jsonify(name='fish', price=290)))
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 200)

    def test_edit_non_existent_order(self):
        rv = self.app.put('/api/v1/orders/-134/', data={'customer': 'hos', 'name': 'rice', 'price': 250})
        result = json.loads(rv.data.decode())
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()
