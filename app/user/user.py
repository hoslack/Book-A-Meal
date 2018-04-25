"""Modelling a user and the two user roles, admin and customer"""


class User(object):
    """This is a super class for a user"""
    def __init__(self, name, email, password, role=None):
        """Initializing the common properties of a user"""
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.name)



