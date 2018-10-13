# app/__init__.py

from flask import Flask

class CustomFlask(Flask):
    instance_relative_config=True
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
      block_start_string='{%',
      block_end_string='%}',
      variable_start_string='((',
      variable_end_string='))',
      comment_start_string='{#',
      comment_end_string='#}',
    ))

# Initialize the app
app = CustomFlask(__name__);
# Configuration
app.config.from_object('config')

# Load the api endpoints
from app import service

# Load the views
from app import views
