from flask import request, session, jsonify
from app.user.user import User
from app import app


registered_users = []
admin = User(name='admin', email='admin@gmail.com', password='1234', admin=True)
registered_users.append(admin)


@app.route('/')
def index():
    """For testing the application on the browser during development"""
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
        else:
            return False


@app.route('/api/v1/meals/', methods=['GET'])
def get_meals():
    """A route for getting all the available meals by the admin"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    if not current_user.admin:
        return jsonify({'message': 'Only admin can view the meals'})
    meals = current_user.get_meals()
    return meals


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    """A route for getting all the orders by the admin"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    if not current_user.admin:
        return jsonify({'message': 'Only admin can view the orders'})
    orders = current_user.get_orders()
    return orders


@app.route('/api/v1/meals', methods=['POST'])
def add_meal():
    """A route for adding a meal into the application"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    if not current_user.admin:
        return jsonify({'message': 'Only admin can view the orders'})
    if not request.form:
        return jsonify({'message': 'No data provided'})
    meal_name = request.form['name']
    meal_price = request.form['price']
    result = current_user.add_meal(meal_name, meal_price)
    return result


@app.route('/api/v1/meals/<int:meal_id>/', methods=['DELETE'])
def delete_meal(meal_id):
    """This method removes a meal from the list of available meals"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    if not current_user.admin:
        return jsonify({'message': 'Only admin can delete meal'})
    result = current_user.delete_meal(meal_id=meal_id)
    return result


@app.route('/api/v1/menu/', methods=['POST'])
def create_menu():
    """A method to add a meal option to the menu list by admin"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    if not current_user.admin:
        return jsonify({'message': 'Only admin can create a menu'})
    meal1 = request.form['meal1']
    meal2 = request.form['meal2']
    total_price = request.form['total_price']
    result = current_user.create_menu(meal1=meal1, meal2=meal2, total_price=total_price)
    return result


@app.route('/api/v1/menu/', methods=['GET'])
def get_menu():
    """A method that allows an authenticated user to get the menu, list of meal options"""
    current_user = session_user()
    if not current_user:
        return jsonify({'message': 'Please Login first'})
    result = current_user.get_menu()
    return result
