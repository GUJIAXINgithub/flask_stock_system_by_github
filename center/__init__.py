from flask import Blueprint

center_blue = Blueprint('center', __name__, url_prefix='/center')

from .views import *
