class Order(object):
    """Modelling the class order that will hold the meals"""

    def __init__(self, customer_name, meal):
        self.customer_name = customer_name
        self.meal = meal

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.meal)
