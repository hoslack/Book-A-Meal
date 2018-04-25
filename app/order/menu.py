"""Modelling the class menu that will hold the meals"""


class Menu(object):
    def __init__(self, menu_date):
        self.menu_date = menu_date
        self.meals = []

    def add_meals(self, new_meals):
        """A method to add a single item to the bucket lists"""
        self.meals.append(new_meals)
        return 'Meals have been added successfully'

    def get_menu(self):
        """A method to return all the meals in the menu"""
        return self.meals

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.menu_date)
