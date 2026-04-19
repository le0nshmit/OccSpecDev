import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, TestingConfig, ProductionConfig

from dotenv import load_dotenv
load_dotenv() # load environment

db = SQLAlchemy() # create database object

def create_app():
    """Initialises flask application and returns it."""


    app = Flask(__name__) # flask application

    env = os.getenv("FLASK_ENV", "development") # get environment variable

    # map environment variables to config environments
    config_map = {
        'development' : DevelopmentConfig,
        'testing'     : TestingConfig,
        'production'  : ProductionConfig
    }

    # import config environment
    app.config.from_object(config_map.get(env, DevelopmentConfig))

    db.init_app(app)      # initialise database with flask application   

    '''import blueprints'''
    from .modules.general import general_bp
    from .modules.authentication import auth_bp, auth_api
    from .modules.store import store_bp, store_api
    from .modules.admin import admin_bp, admin_api

    '''register blueprints with flask application'''
    app.register_blueprint(general_bp)

    app.register_blueprint(store_bp, url_prefix='/store')
    app.register_blueprint(store_api, url_prefix='/api/store')

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(auth_api, url_prefix='/api/auth')

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(admin_api, url_prefix='/api/admin')
    
    with app.app_context():
        db.create_all()

    return app

