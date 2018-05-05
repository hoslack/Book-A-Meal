""" This is meant to show user how to use the API"""

import os
from flasgger import Swagger
from app import app

swagger = Swagger(app)


@app.route('/api/v1/auth/signup/', methods=["POST"])
def signup():
    """ endpoint for registering users.
    ---
    parameters:
      - name: name
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    """


@app.route('/api/v1/auth/login', methods=["POST"])
def login():
    """ endpoint for logging in users.
    ---
    parameters:
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    """


@app.route('/api/v1/meals', methods=["POST"])
def add_meal():
    """ endpoint for creating a meal.
    ---
    parameters:
      - name: name
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
    """


@app.route("/api/v1/meals", methods=["GET"])
def get_meals():
    """endpoint for getting all meals.
    No parameters
    """


@app.route('/api/v1/meals/<int:meal_id>', methods=["PUT"])
def update_meal():
    """ endpoint for updating a meal.
    ---
    parameters:
      - name: meal
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
      - name: meal_id
        in: path
        type: integer
        required: true
    """


@app.route('/api/v1/meals/<int:meal_id>', methods=["DELETE"])
def delete_meal():
    """ endpoint for deleting a meal.
    ---
    parameters:
      - name: meal_id
        in: path
        type: integer
        required: true
    """


@app.route('/api/v1/menu', methods=["POST"])
def create_menu():
    """ endpoint for creating a menu item.
    ---
    parameters:
      - name: meal1
        required: true
        in: formData
        type: string
      - name: meal2
        required: true
        in: formData
        type: string
      - name: total_price
        in: formData
        type: float
        required: true
    """
    

@app.route("/api/v1/menu", methods=["GET"])
def get_menu():
    """endpoint for  getting all menu options.
    No parameters required
    """


@app.route('/api/v1/orders', methods=["POST"])
def create_order():
    """ endpoint for creating an order item.
    ---
    parameters:
      - name: meal1
        required: true
        in: formData
        type: string
      - name: meal2
        required: true
        in: formData
        type: string
      - name: total_price
        in: formData
        type: float
        required: true
    """


@app.route("/api/v1/orders", methods=["GET"])
def get_orders():
    """endpoint for  getting all orders.
    No parameters required
    """


@app.route('/api/v1/orders/<int:order_id>', methods=["PUT"])
def update_order():
    """ endpoint for updating an existing order.
    ---
    parameters:
      - name: meal1
        required: true
        in: formData
        type: string
      - name: meal2
        required: true
        in: formData
        type: string
      - name: total_price
        in: formData
        type: float
        required: true
      - name: order_id
        in: path
        type: integer
        required: true
    """


@app.route('/')
def home():
    """test home route"""
    return "To view the docs visit: https://<heroku-url>/apidocs"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run('', port=port)

