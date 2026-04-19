from flask import render_template, session, redirect
from . import store_bp

def register_store_bp(store_bp):
    @store_bp.route('/market')
    def store():
        '''Creates store home page'''

        # redirect user to auth if not logged in
        if 'user_id' not in session:
            return redirect('/auth/authentication')
        
        return render_template('store.html')