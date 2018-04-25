from app.user.user import User
from app.user.admin import Admin
from app.order.order import Order


class Customer(User):
    """add role property to customer"""
    def __init__(self, name, email, password, role='customer'):
        User.__init__(name, email, password)
        self.role = role

    def get_menu(self):
        menu = Admin.get_menu()
        return menu

    def __repr__(self):
        """Represent the admin using name"""
        return '{}'.format(self.name)
