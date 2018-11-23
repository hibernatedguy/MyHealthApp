from flask.views import MethodView
from flask import jsonify, Response
from bson.json_util import dumps

from .models import reports_doc
from utils.response_handler import CreateResponse, Response404
from flask import request


class ReportsAPI(MethodView):

    def get(self, username):
        if username:
            reports = dumps(reports_doc.fetch_reports_document(username))
            if not reports:
                return Response404(response=username)
            return Response(reports, mimetype='application/json')
        reports = dumps(reports_doc.fetch_reports_document())
        return Response(reports, mimetype='application/json')

    def post(self):
        request_data = request.get_json()
        report_id = reports_doc.create_reports_document(request_data)
        return CreateResponse({'report_id': '{}'.format(report_id)})

    def delete(self, user_id):
        # delete a single user
        return jsonify({'details': '{} DELETE hello world'.format(user_id)})

    def put(self, user_id):
        # delete a single user
        return jsonify({'details': '{} PUT hello world'.format(user_id)})
