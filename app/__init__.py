from flask import Flask
from flask_login import LoginManager

from Config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'


def create_app(config=Config()):
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.main.views import main
    app.register_blueprint(main)

    return app
