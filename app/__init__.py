from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config_options
import os

app = Flask(__name__)


login_manager = LoginManager(app)


mail = Mail(app)
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'

db = SQLAlchemy()
def create_app(config_name):

    #App configurations
    app.config.from_object(config_options[config_name])

    # Registering blueprint
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    # Initializin the app
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap = Bootstrap(app)
    mail.init_app(app)
    
    return app
