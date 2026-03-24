from flask import Blueprint

# authentication blueprint for pages general module
auth_bp = Blueprint('authentication', __name__, template_folder='templates') 

from . import page_routes