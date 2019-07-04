from flask import Blueprint

index_blue = Blueprint('index', __name__, url_prefix='/index')

from .views import *