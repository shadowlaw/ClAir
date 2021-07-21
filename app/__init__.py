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

    from app.blueprints.main.views import main
    from app.blueprints.main.api import main_api
    from app.blueprints.permit.views import permit
    app.register_blueprint(main)
    app.register_blueprint(main_api, url_prefix='/api')
    app.register_blueprint(permit, url_prefix="/permit")

    return app
