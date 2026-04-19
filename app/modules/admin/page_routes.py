from flask import render_template, session, redirect

def register_admin_bp(admin_bp):
    @admin_bp.route('/dashboard', methods=['GET'])
    def dashboard():
        if 'user_id' not in session or session['user_type'] != 'producer':
            return redirect('/auth/authentication')

        return render_template('dashboard.html')
    
    @admin_bp.route('/dashboard/orders')
    def orders():
        return render_template('dashboard-orders.html')
