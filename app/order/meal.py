"""Modelling the Meal class"""
import uuid


class Meal(object):
    def __init__(self, name, price):
        """Initiating the class properties"""
        self.id = uuid.uuid4().int  # generate unique id for the meal
        self.name = name
        self.price = price

    def __repr__(self):
        """Represent meal using name"""
        return '{}'.format(self.name)

