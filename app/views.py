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
    email = request_data['email']
    password = request_data['password']
    for user in registered_users:
        if user.email == email:
            if user.password == password:
                session['logged_in'] = True
                session['user'] = email
                return 'Login  was successful'
            else:
                return "Wrong Username or Password"
    return "You are not a registered user. Please register."

@app.route('/api/v1/')