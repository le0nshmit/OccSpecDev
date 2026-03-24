from flask import render_template
from . import store_bp

@store_bp.route('/store')
def index():
    return render_template('store.html')