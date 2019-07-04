from flask import Blueprint

update_blue = Blueprint('update', __name__, url_prefix='/update')

from .views import *