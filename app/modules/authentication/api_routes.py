from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request, session, redirect
from werkzeug.datastructures import MultiDict
from .schemas import ValidationForm
from ...models import Users
from app import db
import sqlalchemy
import requests



def register_auth_api(auth_api):
    """Creates api routes"""

    @auth_api.route('/validate-input', methods=['POST'])
    def validate():
        '''Validation Endpoint'''

        # retrieve data from frontend
        data = request.get_json()

        # input data into validation form
        form = ValidationForm(MultiDict(data))


        # if form is valid
        if form.validate():

            # hash password and store user in database
            user = Users(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data), phone=form.phone.data, type=form.type.data, address_line=None, postcode=None)
            db.session.add(user)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                return jsonify({"success": False, "errors": {"email": ["Email already exists!"]}}), 400
            return jsonify({"success": True, "message": "Validation Passed"}), 200
        else:
            return jsonify({"success": False, "errors": form.errors}), 400
            

    @auth_api.route('/login', methods=['POST', 'GET'])
    def login():
        '''Login Endpoint'''

        data = request.get_json()

        try:
            user = db.session.execute(db.select(Users).filter_by(email=data['email'])).scalar_one()
        except sqlalchemy.exc.NoResultFound:
            return jsonify({'success': False, 'message': 'Email not found!'}), 401

        if (check_password_hash(user.password, data['password'])):
            session['user_id'] = user.id
            session['user_type'] = user.type


            
            if user.type == 'producer':
                return jsonify({'success': True, 'redirect': '/admin/dashboard'})
            else:
                return jsonify({'success': True, 'redirect': '/store'})

        else:
            return jsonify({'success': False, 'message': 'Password is not correct!'}), 401

