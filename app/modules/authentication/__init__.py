from flask import Blueprint

# authentication blueprint for pages general module
auth_bp = Blueprint('authentication', __name__, template_folder='templates') 
api_bp = Blueprint('auth_api', __name__)

from .page_routes import register_auth_bp
from .api_routes import register_api_bp

register_auth_bp(auth_bp)
register_api_bp(api_bp)