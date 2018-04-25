from app.user.user import User


class Customer(User):
    """add role property to customer"""
    def __init__(self, name, email, password, role='customer'):
        User.__init__(name, email, password)
        self.role = role

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.name)
