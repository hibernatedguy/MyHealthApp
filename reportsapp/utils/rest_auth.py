import requests
from requests.auth import HTTPBasicAuth

from flask.views import MethodView
from flask import jsonify, request

from config.settings import AUTHENTICATION_SERVER_URL


__all__ = ['RestAuthAPI']


class RestAuthAPI(MethodView):
    def get(self):
        import ipdb;ipdb.set_trace()
        auth = request.authorization
        if auth and auth.password and auth.username:
            _request = requests.get(AUTHENTICATION_SERVER_URL, auth=HTTPBasicAuth(auth.username, auth.password))
            res = _request.json()
            return jsonify(res)
        return jsonify({'details': 'Please provide valid information'})
