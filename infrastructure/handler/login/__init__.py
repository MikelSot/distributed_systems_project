from flask import Blueprint

my_blue_user = Blueprint('my_blue_user', __name__)
from . import routes
