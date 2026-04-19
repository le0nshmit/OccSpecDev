from flask import Blueprint

# authentication blueprints
auth_bp = Blueprint('authentication', __name__, template_folder='templates') # pages blueprint
auth_api = Blueprint('auth_api', __name__) # api blueprints

# import functions to register routes with blueprints (avoids circular import)
from .page_routes import register_auth_bp 
from .api_routes import register_auth_api

register_auth_bp(auth_bp)
register_auth_api(auth_api)