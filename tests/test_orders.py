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
        result = self.app.get('/api/v1/orders/')
        self.assertEqual(result.status_code, 200)

    def test_get_all_orders_has_json(self):
        result = self.app.get('/api/v1/orders/')
        self.assertEqual(result.content_type, 'application/json')

    def test_orders_is_dict(self):
        result = self.app.get('/api/v1/orders/')
        self.assertIsInstance(result.data, list)

    def test_add_order_status_code(self):
        result = self.app.post('/api/v1/orders/', data=self.order)
        self.assertEqual(result.status_code, 201)

    def test_add_order_success_response(self):
        result = self.app.post('/api/v1/orders/', data=self.order)
        self.assertIn(b'Success', result.data)

    def test_add_order_without_data(self):
        result = self.app.post('/api/v1/orders/')
        self.assertNotEqual(result.status_code, 200)

    def test_edit_order_status_code(self):
        self.app.post('/api/v1/orders/', data=Order('hos', jsonify(name='rice', price=290)))
        result = self.app.put('/api/v1/orders/<int:id>/', data=Order('hos', jsonify(name='fish', price=290)))
        self.assertEqual(result.status_code, 200)

    def test_edit_non_existent_order(self):
        result = self.app.put('/api/v1/orders/-134/', data={'customer': 'hos', 'name': 'rice', 'price': 250})
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()
