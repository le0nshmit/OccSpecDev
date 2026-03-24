from flask import jsonify
from . import api_bp

def register_api_bp(auth_bp):
    @api_bp.route('/')
    def index():
        data = {'name' : 'leon'}
        return jsonify(data)
