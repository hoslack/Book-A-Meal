from flask import request
from app.user.customer import Customer
from app import app


registered_users = []


@app.route('/api/v1/')
def index():
    return 'Hello World'


@app.route('/api/v1/auth/signup/', methods=['POST'])
def signup():
    request_data = request.get_json()
    name = request_data['name']
    email = request_data['email']
    password = request_data['password']

    for user in registered_users:
        if user.email == email:
            raise Exception('User already exists, login instead')
    new_customer = Customer(name=name, email=email, password=password)
    registered_users.append(new_customer)
    return 'User registration successful'
