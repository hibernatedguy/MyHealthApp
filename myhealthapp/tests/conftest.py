import pytest
from config.settings import secrets

# create environment
from config import create_app

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

# Authorization Decorator
from applications.common.decorators import token_required


@pytest.fixture(scope='module')
def test_client():

    app = create_app('TESTING')
    sql_alch_db = SQLAlchemy(app)

    # Application Views
    rest_auth_view = RestAuthView.as_view('rest_auth_api')
    user_view = UserMethodView.as_view('user_api')
    checkups_view = UserCheckupMethodView.as_view('checkups_api')
    checkup_reports_view = BulkCheckupReportMethodView.as_view('checkup_reports_api')


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


    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
