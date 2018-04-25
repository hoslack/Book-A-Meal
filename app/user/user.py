"""Modelling a user and the two user roles, admin and customer"""


class User(object):
    """This is a super class for a user"""
    def __init__(self, name, email, password):
        """Initializing the common properties of a user"""
        self.name = name
        self.email = email
        self.password = password


class Admin(User):
    """add role property to admin"""
    def __init__(self, name, email, password, role='admin'):
        User.__init__(name, email, password)
        self.role = role

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.name)


class Customer(User):
    """add customer property to admin"""
    def __init__(self, name, email, password, role='customer'):
        User.__init__(name, email, password)
        self.role = role

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.name)
