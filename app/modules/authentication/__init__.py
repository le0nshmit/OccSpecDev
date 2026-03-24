from flask import Blueprint

# authentication blueprint for pages general module
auth_bp = Blueprint('authentication', __name__, template_folder='templates') 
api_bp = Blueprint('auth_api', __name__)

from . import page_routes
from . import api_routes