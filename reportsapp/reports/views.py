from flask.views import MethodView
from flask import jsonify


class ReportsAPI(MethodView):

    def get(self):
        return jsonify({'details': 'GET hello world'})

    def post(self):
        return jsonify({'details': 'POST hello world'})

    def delete(self, user_id):
        # delete a single user
        return jsonify({'details': '{} DELETE hello world'.format(user_id)})

    def put(self, user_id):
        # delete a single user
        return jsonify({'details': '{} PUT hello world'.format(user_id)})
