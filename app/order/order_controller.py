"""Modelling the super class that does every action"""
from flask import jsonify
from app.order.meal import Meal
from app.order.menu import MenuItem
from app.order.order import Order


class OrderController(object):
    def __init__(self):
        self.sample_meal = Meal(name='rice', price=120)
        self.sample_order_item = Order(customer_name="hoslack", meal1="rice", meal2="beef", total_price=125)
        self.sample_menu_item = MenuItem(meal1="rice", meal2="beef", total_price=300)
        self.meals = [self.sample_meal]
        self.orders = [self.sample_order_item]
        self.menu = [self.sample_menu_item]

    def add_meal(self, meal_name, meal_price):
        """A method to add a single meal to the application"""
        for n in self.meals:
            if meal_name == n.name:
                return jsonify({'message': '{} already exists'.format(meal_name)})
        new_meal = Meal(name=meal_name, price=meal_price)
        self.meals.append(new_meal)
        return jsonify({'message': 'Meal has been added successfully', 'id': new_meal.id})

    def update_meal(self, meal_id, meal_name, meal_price):
        """A method for editing an existing meal"""
        available_meal = [n for n in self.meals if n.id == meal_id]
        if available_meal:
            meal = available_meal[0]
            meal.name = meal_name
            meal.price = meal_price
            return jsonify({'message': 'Meal edited successfully'})
        else:
            return jsonify({'message': 'Meal does not exist'})

    def delete_meal(self, meal_id):
        """A method to delete a meal from the application"""
        meal = [n for n in self.meals if n.id == meal_id]
        if meal:
            self.meals.remove(meal[0])
            return jsonify({'message': 'Meal deleted successfully'})
        else:
            return jsonify({'message': 'Meal does not exist'})

    def get_meals(self):
        """A method to retrieve and show all the meals in the application"""
        meals = []
        for n in self.meals:
            meals.append({"meal_id": n.id, "meal_name": n.name, "meal_price": n.price})
        return jsonify({'data': meals})

    def create_menu(self, meal1, meal2, total_price):
        menu_item = MenuItem(meal1=meal1, meal2=meal2, total_price=total_price)
        item = [n for n in self.menu if n == menu_item]
        if item:
            return jsonify({'message': '{} already exists'.format(item)})
        self.menu.append(menu_item)
        return jsonify({'message': 'Menu Item added successfully'})

    def create_orders(self, customer_name, meal1, meal2, total_price):
        """A method to create an order, by a customer"""
        order = Order(customer_name=customer_name, meal1=meal1, meal2=meal2, total_price=total_price)
        self.orders.append(order)
        return jsonify({'message': 'Order added successfully'})

    def update_order(self, order_id, meal1, meal2, total_price):
        """A method to modify the details of an order already made"""
        order_available = [n for n in self.orders if n.id == order_id]
        # find the order by id
        if order_available:
            order = order_available[0]
            order.meal1 = meal1
            order.meal2 = meal2
            order.total_price = total_price
            return jsonify({'message': 'Order edited successfully'})
        return jsonify({'message': 'Order does not exist'})

    def get_orders(self):
        """A method that returns all the orders in the app"""
        orders = []
        for n in self.orders:
            orders.append({"order_id": n.id, "customer_name": n.customer_name, "meal1": n.meal1, "meal2": n.meal2,
                           "meal_price": n.total_price})
        return jsonify({'data': orders})

    def get_menu(self):
        """A method to retrieve and show all the options in the menu"""
        menu = []
        for n in self.menu:
            menu.append({"meal1": n.meal1, "meal2": n.meal2, "total_price": n.total_price})
        return jsonify({'data': menu})






