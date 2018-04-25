"""Modelling the admin"""
from app.user.user import User
from app.order.meal import Meal
from app.order.order import Order
from app.order.menu import Menu


class Admin(User):
    """add role property to admin"""
    def __init__(self, name, email, password, role='admin'):
        User.__init__(name, email, password)
        self.role = role
        self.meals = []
        self.orders = []
        self.menu = []

    def add_meal(self, meal_name, meal_price):
        """A method to add a single meal to the application"""
        if meal_name in self.meals:
            raise Exception('{} already exists'.format(meal_name))
        new_meal = Meal(name=meal_name, price=meal_price)
        self.meals.append(new_meal)
        return '{} has been added successfully'.format(meal_name)

    def update_meal(self, meal_id, meal_name, meal_price):
        """A method for editing an existing meal"""
        for n in self.meals:
            if n.id == meal_id:
                n.name = meal_name
                n.price = meal_price
                return 'Meal edited successfully'
            else:
                raise Exception('The meal does not exist')

    def delete_meal(self, meal_id):
        """A method to delete a meal from the application"""
        for n in self.meals:
            if n.id == meal_id:
                self.meals.remove(n)
                return 'Meal deleted successfully'
            else:
                raise Exception('The meal does not exist')

    def get_all_meals(self):
        """A method to retrieve and show all the meals in the application"""
        return self.meals

    def create_menu(self, meal_list):
        if not isinstance(meal_list, list):
            raise Exception('Meals need to be in a list')
        Menu.add_meals(meal_list)
        return 'Meals added successfully'

    def get_orders(self):
        return self.orders

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.name)
