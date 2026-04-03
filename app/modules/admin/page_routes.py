from flask import render_template, session, redirect

def create_page_routes(admin_bp):
    @admin_bp.route('/dashboard', methods=['GET'])
    def dashboard():
        if 'user_id' not in session or session['user_type'] != 'producer':
            return redirect('/auth/authentication')

        return render_template('dashboard.html')
