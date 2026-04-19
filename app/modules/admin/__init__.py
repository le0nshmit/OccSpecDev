from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')
admin_api = Blueprint('admin_api', __name__)

from .page_routes import register_admin_bp
from .api_routes import register_admin_api

register_admin_bp(admin_bp)
register_admin_api(admin_api)