from flask import render_template, request, session, redirect
from . import auth_bp

def register_auth_bp(auth_bp):
    """Creates page routes"""

    @auth_bp.route('/authentication', methods=['POST', 'GET'])
    def auth(): 
        if 'user_id' in session:
            return redirect('/store')

        return render_template('authentication.html') 
    

    @auth_bp.route('/logout', methods=['POST', 'GET'])
    def logout():
        '''Logout Endpoint'''

        session.clear()
        return redirect('/auth/authentication')
