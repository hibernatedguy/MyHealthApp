# import unittest

from flask_script import Manager

# create environment
from config import get_app_and_db
from config.settings import secrets

# views import
from reports.views import *
from utils.rest_auth import *

# models registration
app, mongo_db = get_app_and_db(secrets.get('ENVIRONMENT'))

# application URLs registration
user_view = UserAPI.as_view('user_api')
report_view = ReportsAPI.as_view('report_api')
user_report_view = UserReportsAPI.as_view('user_report_api')
rest_auth_view = RestAuthAPI.as_view('rest_auth_api')


# Users
# TODO : Cleanup
app.add_url_rule('/users/', defaults={'username': None}, view_func=user_view, methods=['GET', ])
app.add_url_rule('/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/users/<string:username>/', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

# User based reports
app.add_url_rule('/users/<string:username>/reports/', view_func=user_report_view, methods=['GET'])

# Reports
# TODO : Cleanup
app.add_url_rule('/reports/', view_func=report_view, methods=['GET', 'POST'])

app.add_url_rule('/login/', view_func=rest_auth_view, methods=['GET'])


# Manager Commands
manager = Manager(app)


@manager.command
def runserver():
    app.run(port=8080)


if __name__ == '__main__':
    manager.run()
