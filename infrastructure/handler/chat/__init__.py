from flask import Blueprint

my_blue_message = Blueprint('my_blue_message', __name__)
from . import routes
