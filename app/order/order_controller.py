"""Modelling the super class that does every action"""
from flask import jsonify
from app.order.meal import Meal
from app.order.menu import MenuItem
from app.order.order import Order


class OrderController(object):
    def __init__(self):
        self.meals = []
        self.orders = []
        self.menu = []

    def add_meal(self, meal_name, meal_price):
        """A method to add a single meal to the application"""
        if meal_name in self.meals:
            return jsonify({'message': '{} already exists'.format(meal_name)})
        new_meal = Meal(name=meal_name, price=meal_price)
        self.meals.append(new_meal)
        return jsonify({'message': '{} has been added successfully'.format(meal_name)})

    def update_meal(self, meal_id, meal_name, meal_price):
        """A method for editing an existing meal"""
        meal = [n for n in self.meals if n.id == meal_id]
        if meal:
            meal.name = meal_name
            meal.price = meal_price
            return jsonify({'message': 'Meal edited successfully'})
        else:
            return jsonify({'message': 'Meal does not exist'})

    def delete_meal(self, meal_id):
        """A method to delete a meal from the application"""
        meal = [n for n in self.meals if n.id == meal_id]
        if meal:
            self.meals.remove(meal)
            return jsonify({'message': 'Meal deleted successfully'})
        else:
            return jsonify({'message': 'Meal does not exist'})

    def get_meals(self):
        """A method to retrieve and show all the meals in the application"""
        return jsonify({'data': self.meals})

    def create_menu(self, meal1, meal2, total_price):
        menu_item = MenuItem(meal1=meal1, meal2=meal2, total_price=total_price)
        item = [n for n in self.menu if n == menu_item]
        if item:
            return jsonify({'message': '{} already exists'.format(item)})
        self.menu.append(menu_item)
        return jsonify({'message': 'Menu Item added successfully'})

    def create_orders(self, customer_name, meal_name, meal_price):
        """A method to create an order, by a customer"""
        order = Order(customer_name=customer_name, meal_name=meal_name, price=meal_price)
        self.orders.append(order)
        return jsonify({'message': 'Order added successfully'})

    def update_order(self, order_id, meal_name, meal_price):
        """A method to modify the details of an order already made"""
        order = [n for n in self.orders if n.id == order_id]
        # find the order by id
        if order:
            order.meal_name = meal_name
            order.price = meal_price
            return jsonify({'message': 'Order edited successfully'})
        return jsonify({'message': 'Order does not exist'})

    def get_orders(self):
        """A method that returns all the orders in the app"""
        return jsonify({'data': self.orders})

    def get_menu(self):
        """A method to retrieve and show all the options in the menu"""
        return jsonify({'data': self.meals})






