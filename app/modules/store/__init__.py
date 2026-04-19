from flask import Blueprint

# store blueprint for pages general module
store_bp = Blueprint('store', __name__, template_folder='templates') 
store_api = Blueprint('store_api', __name__)

from .api_routes import register_store_api
from .page_routes import register_store_bp

register_store_api(store_api)
register_store_bp(store_bp)