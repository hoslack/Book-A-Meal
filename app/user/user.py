"""Modelling a user with two user roles, admin and customer who is also the controler of the app"""
from app.order.order_controller import OrderController


class User(OrderController):
    """This is a super class for a user"""

    def __init__(self, name, email, password, admin=False):
        OrderController.__init__(self)
        """Initializing the properties of a user"""
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
