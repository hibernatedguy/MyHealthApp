# import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# create environment
from config import db, create_app
from config.settings import secrets

from applications.profiles.views import UserAPI

# models registration
from applications.profiles.models import *
from applications.machines.models import *
from applications.checkups.models import *
from applications.common.models import *

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = create_app(secrets.get('ENVIRONMENT', 'DEVELOPMENT'))


# application URLs registration
user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', view_func=user_view, methods=['GET', 'POST'])
app.add_url_rule('/users/<int:user_id>/', view_func=user_view, methods=['PUT', 'DELETE'])


# Manager Commands
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


sql_alch_db = SQLAlchemy(app)

# admin
admin = Admin(app)
admin.add_view(ModelView(User, sql_alch_db.session))
admin.add_view(ModelView(Machine, sql_alch_db.session))
admin.add_view(ModelView(Checkup, sql_alch_db.session))
admin.add_view(ModelView(Disease, sql_alch_db.session))


@manager.command
def runserver():
    app.run()


# @manager.command
# def test():
#     """Runs the unit tests."""
#     tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1


if __name__ == '__main__':
    sql_alch_db.create_all()
    manager.run()
