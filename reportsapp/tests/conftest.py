import pytest
from config import get_app_and_db, secrets

# views import
from reports.views import *


@pytest.fixture(scope='module')
def test_client():
    # app = create_app('flask_test.cfg')
    app, mongo_db = get_app_and_db(secrets.get('ENVIRONMENT'))

    # test conf
    # application URLs registration
    user_view = UserAPI.as_view('user_api')
    report_view = ReportsAPI.as_view('report_api')
    user_report_view = UserReportsAPI.as_view('user_report_api')

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

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
