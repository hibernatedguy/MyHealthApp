# import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# create environment
from config import db, create_app
from config.settings import secrets
from config.flask_celery import make_celery

# Views
from applications.profiles.views import *

# Models registration
from applications.profiles.models import *
from applications.machines.models import *
from applications.checkups.models import *
from applications.common.models import *

# Admin registration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# TASKS
# import reporting tasks to run in background
from reporting_tasks import *

app = create_app(secrets.get('ENVIRONMENT'))
celery = make_celery(app)
sql_alch_db = SQLAlchemy(app)

# application URLs registration
userview_method = UserMethodView.as_view('user_api')
app.add_url_rule('/users/', defaults={'username': None}, view_func=userview_method, methods=['GET'])
app.add_url_rule('/users/', view_func=userview_method, methods=['POST'])
app.add_url_rule('/users/<string:username>/', view_func=userview_method, methods=['GET', 'PUT', 'DELETE'])


# Manager Commands
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Admin
admin = Admin(app)
admin.add_view(ModelView(User, sql_alch_db.session))
admin.add_view(ModelView(Machine, sql_alch_db.session))
admin.add_view(ModelView(Checkup, sql_alch_db.session))
admin.add_view(ModelView(Disease, sql_alch_db.session))


@manager.command
def runserver():
    app.run()


if __name__ == '__main__':
    sql_alch_db.create_all()
    manager.run()
