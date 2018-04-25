from flask import request, session
from app.user.user import User
from app import app


registered_users = []


@app.route('/')
def index():
    return 'Hello World'


@app.route('/api/v1/auth/signup/', methods=['POST'])
def signup():
    """A method for creating an account for the user from the json data given"""

    if not request.form:
        return 'No data received'
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    for user in registered_users:
        if user.email == email:
            return 'User already exists, login instead'
    new_customer = User(name=name, email=email, password=password)
    registered_users.append(new_customer)
    return 'User registration successful'


@app.route('/api/v1/auth/login/', methods=['POST'])
def login():
    """A method for loging in a user who provides the correct credentials and is registered"""
    request_data = request.form
    if not request_data:
        return 'No data received'
    email = request.form['email']
    password = request.form['password']
    for user in registered_users:
        if user.email == email:
            if user.password == password:
                session['logged_in'] = True
                session['user'] = email
                return 'Login  was successful'
            else:
                return "Wrong Username or Password"
    return "You are not a registered user. Please register."

def session_user():
    """Get the current user"""
    for user in registered_users:
        if user.email == session['user']:
            return user


@app.route('/api/v1/meals/', methods=['GET'])
def get_meals():
    """A route for getting all the available meals by the admin"""
    current_user = session_user()
    if not current_user:
        return 'Please Login first'
    if current_user.role != 'admin':
        return 'Only admin can view the meals'
    return current_user.meals

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    """A route for getting all the orders by the admin"""
    current_user = session_user()
    if not current_user:
        return 'Please Login first'
    if current_user.role != 'admin':
        return 'Only admin can view the orders'
    return current_user.orders


@app.route('/api/v1/meals', methods=['POST'])
def add_meal():
    """A route for adding a meal into the application"""
    current_user = session_user()
    if not current_user:
        return 'Please Login first'
    if current_user.role != 'admin':
        return 'Only admin can add meals'
    if not request.form:
        return 'No data provided '
    meal_name = request.form['name']
    meal_price = request.form['price']
    current_user.add_meal(meal_name, meal_price)
    return 'Meal created successfully'
