from flask import jsonify, request, session, redirect

def register_store_api(store_api):
    """Creates api routes"""

    @store_api.route('/dashboard-nav-options', methods=['POST'])
    def dashboard_options():

        from .nav_options import options
        return jsonify({'success':True ,'options' : options})