from flask import render_template, request
from . import auth_bp
from .schemas import RegistrationForm

@auth_bp.route('/authentication', methods=['POST'])
def auth():    
    return render_template('authentication.html')