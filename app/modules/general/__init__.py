from flask import Blueprint

# general blueprint for pages general module
general_bp = Blueprint('general', __name__, template_folder='templates') # general blueprint for pages general module

from . import page_routes