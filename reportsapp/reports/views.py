from flask.views import MethodView
from flask import Response
from bson.json_util import dumps

from .managers import reports_document, users_document
from utils.response_handler import *

from flask import request

__all__ = ['ReportsAPI', 'UserAPI', 'UserReportsAPI']


class UserAPI(MethodView):
    """ APIVIew to manager CRUD for User """

    def validate_data(self, request_data):
        ''' 1-level data validation to check if username is present or not '''
        keys_to_check = ['username']
        missing_keys = []
        if not request_data:
            return 'Please provide {}.'.format(keys_to_check), False

        if request_data:
            for key in keys_to_check:
                if key not in request_data.keys():
                    missing_keys.append(key)
            if missing_keys:
                detail = 'Please provide {}.'.format(missing_keys)
                return detail, False
        return 'OK', True

    def get(self, username):
        """ Fetch User information else return custom responses. """
        if username:
            users = dumps(users_document.fetch_users(username))
            if not users:
                return Response404(response=username)
            return Response(users, mimetype='application/json')
        users = dumps(users_document.fetch_users())
        return Response(users, mimetype='application/json')

    def post(self):
        """ Create User. Not needed now because user's are getting registered from Report API. """
        request_data = request.get_json()

        # validate data
        msg, status = self.validate_data(request_data)
        if not status:
            return BadResponseAlreadyExist(response=msg)

        # get_or_create
        user_id, status = users_document.get_or_create(request_data)
        if status:
            return CreateResponse({'user_id': '{}'.format(user_id)})
        return BadResponseAlreadyExist(response='Username already exist')

    def delete(self, username):
        """ Delete User """
        # fire delete users
        deleted_user_count, deleted_report_count = users_document.delete_users(username)
        details = 'Users : #{} and Reports #{} deleted.'.format(deleted_user_count, deleted_report_count)
        return DeleteResponse(response=details)


class UserReportsAPI(MethodView):
    """
    UserReportAPIView to support nested routers. users/<username>/reports/
    """

    def get(self, username):
        if username:
            reports = dumps(reports_document.fetch_reports(username))
            if not reports:
                return Response404(response=username)
            return Response(reports, mimetype='application/json')
        reports = dumps(reports_document.fetch_reports())
        return Response(reports, mimetype='application/json')


class ReportsAPI(MethodView):

    def get(self, username=None):
        if username:
            reports = dumps(reports_document.fetch_reports(username))
            if not reports:
                return Response404(response=username)
            return Response(reports, mimetype='application/json')
        reports = dumps(reports_document.fetch_reports())
        return Response(reports, mimetype='application/json')

    def post(self):
        report_ids = []
        request_data = request.get_json()
        # using iterator to avoid
        for data in request_data:
            report_id = reports_document.create_reports(data)
            report_ids.append(str(report_id))
        return CreateResponse({'report_ids': report_ids})
