# import unittest

from flask_script import Manager
from flask_pymongo import PyMongo

# create environment
from config import create_app
from config.settings import secrets

# views import
from reports.views import ReportsAPI

# models registration
app = create_app(secrets.get('ENVIRONMENT', 'DEVELOPMENT'))
mongo_db = PyMongo(app)

# application URLs registration
report_view = ReportsAPI.as_view('user_api')
app.add_url_rule('/reports/', defaults={'report_id': None}, view_func=report_view, methods=['GET', ])
app.add_url_rule('/reports/', view_func=report_view, methods=['POST', ])
app.add_url_rule('/reports/<int:report_id>/', view_func=report_view, methods=['GET', 'PUT', 'DELETE'])


# Manager Commands
manager = Manager(app)


@manager.command
def runserver():
    app.run()


if __name__ == '__main__':
    manager.run()
