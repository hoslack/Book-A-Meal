from flask import request, session, jsonify
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
            return jsonify({'message': 'User exists, log in instead'})
    new_customer = User(name=name, email=email, password=password)
    registered_users.append(new_customer)
    return jsonify({'message': 'User registration successful'})


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
                return jsonify({'message': 'Login successful'})
            else:
                return jsonify({'message': "Wrong Username or Password"})
    return jsonify({'message': "You are not a registered user. Please register."})


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
        return jsonify({'message': 'Please Login first'})
    if current_user.role != 'admin':
        return jsonify({'message': 'Only admin can view the meals'})
    meals = current_user.get_meals()
    return meals


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    """A route for getting all the orders by the admin"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    if current_user.role != 'admin':
        return jsonify({'message': 'Only admin can view the orders'})
    orders = current_user.get_orders()
    return orders


@app.route('/api/v1/meals', methods=['POST'])
def add_meal():
    """A route for adding a meal into the application"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    if current_user.role != 'admin':
        return jsonify({'message': 'Only admin can view the orders'})
    if not request.form:
        return jsonify({'message': 'No data provided'})
    meal_name = request.form['name']
    meal_price = request.form['price']
    current_user.add_meal(meal_name, meal_price)
    return jsonify({'message': 'Meal created successfully'})

