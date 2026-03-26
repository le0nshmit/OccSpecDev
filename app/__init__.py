from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    """Initialises flask application and returns it."""

    app = Flask(__name__) # flask application

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///omstamce/app.db'
    
    

    '''import blueprints'''
    from .modules.general import general_bp
    from .modules.authentication import auth_bp, api_bp
    from .modules.store import store_bp

    '''register blueprints with flask application'''
    app.register_blueprint(general_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api/auth')
    
    return app

