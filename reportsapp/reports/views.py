from flask.views import MethodView
from flask import jsonify


class ReportsAPI(MethodView):

    def get(self, report_id):
        # mydict = { "name": "John", "address": "Highway 37", "online": True}
        # mongo.db.users.insert_one(mydict)
        # online_users = mongo.db.users.find({"online": True})
        # for x in online_users:
        #     print(x)
        if report_id:
            return jsonify({'details': '{} GET hello world'.format(report_id)})
        return jsonify({'details': 'GET hello world'})

    def post(self):
        return jsonify({'details': 'POST hello world'})

    def delete(self, user_id):
        # delete a single user
        return jsonify({'details': '{} DELETE hello world'.format(user_id)})

    def put(self, user_id):
        # delete a single user
        return jsonify({'details': '{} PUT hello world'.format(user_id)})
