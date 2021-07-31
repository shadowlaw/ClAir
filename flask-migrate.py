from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app import db

app = create_app()

migrate = Migrate(app, db, render_as_batch=app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'))
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
