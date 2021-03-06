from flask import Flask
from flask_login import LoginManager
from sqlalchemy import MetaData

from Config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
csrf = CSRFProtect()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


def create_app(config=Config()):
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)

    from app.blueprints.main.views import main
    from app.blueprints.main.api import main_api
    from app.blueprints.planning_application.views import planning_application_views
    from app.blueprints.report.views import report_views
    from app.blueprints.admin.views import admin_views
    app.register_blueprint(main)
    app.register_blueprint(main_api, url_prefix='/api')
    app.register_blueprint(planning_application_views, url_prefix="/planning_application")
    app.register_blueprint(report_views, url_prefix="/report")
    app.register_blueprint(admin_views, url_prefix="/admin")

    return app
