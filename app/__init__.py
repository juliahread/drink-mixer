# app/__init__.py

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
# Configuration
app.config.from_object('config')

# Load the api endpoints
from app import service

# Load the views
from app import views
