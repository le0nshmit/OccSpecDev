from flask import jsonify, request, session, redirect
from ...models import Orders
from math import ceil
from app import db

def register_admin_api(admin_api):
    """Creates api routes"""

    @admin_api.route('/dashboard-nav-options', methods=['POST'])
    def dashboard_options():

        from .nav_options import options
        return jsonify({'success':True ,'options' : options})
    
    
    
    @admin_api.route('/dashboard-orders', methods=['POST'])
    def get_orders(page: int=1, per_page: int=5):

        # total amount of orders 
        total_orders = db.session.query(Orders)\
        .filter(Orders.producer_id == session['id'])\
        .count()

        # pages for table (total orders / rows per page)
        pages = ceil(total_orders / per_page) if total_orders > 0 else 0

        # validate page range
        if page < 1:
            page = 1
        elif page > pages and pages > 0:
            page = pages

        # offset 
        offset = (page - 1) * per_page

        # get next 5 orders from offset 
        orders = db.session.query(Orders)\
        .filter(Orders.producer_id == session['id'])\
        .order_by(Orders.created_at.desc())\
        .offset(offset)\
        .limit(per_page)\
        .all()

        
