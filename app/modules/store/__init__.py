from flask import Blueprint

# store blueprint for pages general module
store_bp = Blueprint('store', __name__, template_folder='templates') 

from . import page_routes