"""Modelling the Meal class"""


class Meal(object):
    def __init__(self, name, price):
        """Initiating the class properties"""
        self.name = name
        self.price = price

    def __repr__(self):
        """Represent meal using name"""
        return '{}'.format(self.name)

