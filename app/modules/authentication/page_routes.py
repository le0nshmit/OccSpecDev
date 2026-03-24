from flask import render_template, request
from . import auth_bp

def register_auth_bp(auth_bp):
    @auth_bp.route('/authentication', methods=['POST'])
    def auth():    
        return render_template('authentication.html')