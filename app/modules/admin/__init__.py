from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')

from .page_routes import create_page_routes

create_page_routes(admin_bp)