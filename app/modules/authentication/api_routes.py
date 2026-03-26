from werkzeug.datastructures import MultiDict
from .schemas import ValidationForm
from flask import jsonify, request
from . import api_bp
import requests

def register_api_bp(auth_bp):
    @api_bp.route('/validate', methods=['POST'])
    def validate():
        
        data = request.get_json()

        form = ValidationForm(MultiDict(data))
        
        if form.validate():
            return jsonify({"success": True, "message": "Validation Passed"}), 200
        else:
            return jsonify({"success": False, "errors": form.errors}), 400
