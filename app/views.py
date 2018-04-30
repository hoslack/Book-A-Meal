from flask import request, jsonify, session
from app.user.user import User
from app.order.order_controller import OrderController
from app import app

order_controller = OrderController()
admin = User(name='admin', email='admin@gmail.com', password='1234', admin=True)
registered_users = [admin]
logged_in_user = object


@app.route('/api/v1/')
def index():
    """For testing the application on the browser during development"""
    return jsonify({'message': 'This is the home page'})


@app.route('/api/v1/auth/signup/', methods=['POST'])
def signup():
    """A method for creating an account for the user from the json data given"""

    json_data = request.get_json(force=True)
    if not json_data:
        return jsonify({'message': 'Please enter your credentials'}), 400
    name = json_data['name']
    email = json_data['email']
    password = json_data['password']
    if not name or not email or not password:
        return jsonify({'message': 'Please enter your credentials'}), 400
    for user in registered_users:
        if user.email == email:
            return jsonify({'message': 'User exists, log in instead'}), 409
    new_customer = User(name=name, email=email, password=password)
    registered_users.append(new_customer)
    return jsonify({'message': 'User registration successful'}), 201


@app.route('/api/v1/auth/login/', methods=['POST'])
def login():
    """A method for loging in a user who provides the correct credentials and is registered"""
    session.clear()  # for clearing any remaining session cookie
    json_data = request.get_json(force=True)
    if not json_data:
        return jsonify({'message': 'Please enter your credentials'}), 400
    email = json_data['email']
    password = json_data['password']
    if not email or not password:
        return jsonify({'message': 'Please enter your credentials'}), 400
    for user in registered_users:
        if user.email == email:
            if user.password == password:
                session['logged_in'] = True
                session['user'] = email
                session.modified = True
                return jsonify({'message': 'Login successful', 'user': '{}'.format(session['user'])}), 200
            else:
                return jsonify({'message': "Wrong Email or Password"}), 401
    return jsonify({'message': "You are not a registered user. Please register"}), 401


@app.route('/api/v1/meals/', methods=['GET'])
def get_meals():
    """A route for getting all the available meals by the admin"""
    meals = order_controller.get_meals()
    return meals


@app.route('/api/v1/orders/', methods=['GET'])
def get_orders():
    """A route for getting all the orders by the admin"""
    orders = order_controller.get_orders()
    return orders


@app.route('/api/v1/meals/', methods=['POST'])
def add_meal():
    """A route for adding a meal into the application"""
    json_data = request.get_json(force=True)
    if not json_data:
        return jsonify({'message': 'No data provided'}), 400
    meal_name = json_data['name']
    meal_price = json_data['price']
    result = order_controller.add_meal(meal_name, meal_price)
    return result, 200


@app.route('/api/v1/meals/<int:meal_id>/', methods=['DELETE'])
def delete_meal(meal_id):
    """This method removes a meal from the list of available meals"""
    result = order_controller.delete_meal(meal_id=meal_id)
    return result


@app.route('/api/v1/meals/<int:meal_id>/', methods=['PUT'])
def update_meal(meal_id):
    """This method updates a meal in the list of available meals"""
    json_data = request.get_json(force=True)
    meal_name = json_data['name']
    meal_price = json_data['price']
    result = order_controller.update_meal(meal_id=meal_id, meal_name=meal_name, meal_price=meal_price)
    return result


@app.route('/api/v1/menu/', methods=['POST'])
def create_menu():
    """A method to add a meal option to the menu list by admin"""
    json_data = request.get_json(force=True)
    if not json_data:
        return jsonify({'message': 'No data provided'})
    meal1 = json_data['meal1']
    meal2 = json_data['meal2']
    total_price = json_data['total_price']
    result = order_controller.create_menu(meal1=meal1, meal2=meal2, total_price=total_price)
    return result


@app.route('/api/v1/menu/', methods=['GET'])
def get_menu():
    """A method that allows an authenticated user to get the menu, list of meal options"""
    result = order_controller.get_menu()
    return result, 200


@app.route('/api/v1/orders/', methods=['POST'])
def create_order():
    """A method to create an order by a customer"""
    json_data = request.get_json(force=True)
    if not json_data:
        return jsonify({'message': 'No data provided'})
    customer_name = json_data['customer_name']
    meal1 = json_data['meal1']
    meal2 = json_data['meal2']
    total_price = json_data['total_price']
    result = order_controller.create_orders(customer_name=customer_name, meal1=meal1, meal2=meal2, total_price=total_price)
    return result


@app.route('/api/v1/orders/<int:order_id>/', methods=['PUT'])
def update_order(order_id):
    """A method to modify an existing order by customer"""
    json_data = request.get_json(force=True)
    meal1 = json_data['meal1']
    meal2 = json_data['meal2']
    total_price = json_data['total_price']
    result = order_controller.update_order(order_id=order_id, meal1=meal1, meal2=meal2, total_price=total_price)
    return result
