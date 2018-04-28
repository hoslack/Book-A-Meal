import uuid


class Order(object):
    """Modelling the class order that will hold the meals"""

    def __init__(self, customer_name, meal1, meal2, total_price):
        self.id = uuid.uuid4().int  # generate unique id for the order
        self.customer_name = customer_name
        self.meal1 = meal1
        self.meal2 = meal2
        self.total_price = total_price

    def __repr__(self):
        """Represent the admin using name"""
        return '{} and {}'.format(self.meal1, self.meal2)
