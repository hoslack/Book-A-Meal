from flask import Flask
from config import Config

app = Flask(__name__)
"""Load the views- import the views down here to prevent circular import problems"""
from app import views

"""Load the config file"""
app.config.from_object(Config)
