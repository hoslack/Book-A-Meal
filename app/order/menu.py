"""Modelling the class menu that will hold the meals"""
import uuid


class MenuItem(object):
    def __init__(self, meal1, meal2, total_price):
        self.id = uuid.uuid4()
        self.meal1 = meal1
        self.meal2 = meal2
        self.total_price = total_price

    def __repr__(self):
        """Represent the admin using name"""
        return '{} and {}'.format(self.meal1, self.meal2)


