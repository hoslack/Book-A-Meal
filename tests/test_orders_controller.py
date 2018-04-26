import unittest
from app.order.order_controller import OrderController


class TestOrdersController(unittest.TestCase):
    """This is for testing the main operations performed on meals, orders and menuitems"""
    def setUp(self):
        self.meals = []
        self.menu = []
        self.orders = []
        self.controller = OrderController()
        self.meal_name = 'rice'
        self.price = 230

    def test_deleting_non_existent_meal(self, meal_id):
        """Test for deleting a meal that does not exist"""
        meal = [n for n in self.meals if n.id == meal_id]
        if meal:
            result = self.controller.delete_meal(meal_id)
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.message, 'Deleted Successfully')
        else:
            result = self.controller.delete_meal(meal_id)
            self.assertEqual(result.status_code, 'Meal does not exist')

    def test_edit_non_existent_meal(self, meal_id):
        """Test for editing a non existing meal"""
        meal = [n for n in self.meals if n.id == meal_id]
        if meal:
            result = self.controller.update_meal(meal_id=meal_id, meal_name=self.meal_name, meal_price=self.price)
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.message, 'Updated Successfully')
        else:
            result = self.controller.update_meal(meal_id=meal_id, meal_name=self.meal_name, meal_price=self.price)
            self.assertEqual(result.status_code, 'Meal does not exist')





