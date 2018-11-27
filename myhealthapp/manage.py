# import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# create environment
from config import db, create_app
from config.settings import secrets, SERVER_PORT
from config.flask_celery import make_celery

# Views
from applications.profiles.views import *
from applications.checkups.views import *
from applications.rest_auth.rest_auth import *

# Models registration
from applications.profiles.models import *
from applications.checkups.models import *
from applications.common.models import *

# Admin registration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Authorization Decorator
from applications.common.decorators import token_required

# TASKS
# import reporting tasks to run in background
from reporting_tasks import *


app = create_app(secrets.get('ENVIRONMENT'))
celery = make_celery(app)
sql_alch_db = SQLAlchemy(app)

# Application Views
rest_auth_view = RestAuthView.as_view('rest_auth_api')
user_view = token_required(UserMethodView.as_view('user_api'))
checkups_view = token_required(UserCheckupMethodView.as_view('checkups_api'))
checkup_reports_view = token_required(BulkCheckupReportMethodView.as_view('checkup_reports_api'))


# ---- START OF URLS BLOCK
# user
app.add_url_rule('/users/', defaults={'username': None}, view_func=user_view, methods=['GET'])
app.add_url_rule('/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/users/<string:username>/', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

# checkups
app.add_url_rule('/users/<string:username>/checkups/', view_func=checkups_view, methods=['GET', 'POST'])
app.add_url_rule('/users/<string:username>/checkups/<int:checkup_id>/', view_func=checkups_view,
                 methods=['DELETE'])

# reports
app.add_url_rule('/reports/', view_func=checkup_reports_view, methods=['GET', 'POST'])


# auth URLs
app.add_url_rule('/login/', view_func=rest_auth_view, methods=['GET'])
app.add_url_rule('/registration/', view_func=rest_auth_view, methods=['POST'])

# ---- END OF URLS BLOCK

# Manager Commands
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Admin
admin = Admin(app)
admin.add_view(ModelView(User, sql_alch_db.session))
admin.add_view(ModelView(Checkup, sql_alch_db.session))


@manager.command
def runserver():
    app.run(port=SERVER_PORT)


if __name__ == '__main__':
    sql_alch_db.create_all()
    manager.run()
