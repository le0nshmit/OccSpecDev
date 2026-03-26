from flask import jsonify
from . import api_bp

@api_bp.route('/')
def index():
    data = {'name' : 'leon'}
    return jsonify(data)
