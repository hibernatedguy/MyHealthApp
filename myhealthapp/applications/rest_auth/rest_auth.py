import jwt
import datetime

from flask.views import MethodView
from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash

from config.settings import secrets
from ..profiles.models import User


__all__ = ['LoginView']


class LoginView(MethodView):
    def get(self):
        auth = request.authorization
        if auth and auth.password and auth.username:
            user = User.query.filter_by(username=auth.username).first()

            if not user:
                return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

            if check_password_hash(user.password, auth.password):
                token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                                            secrets.get('SECRET_KEY'))
                return jsonify({'token': token.decode('UTF-8')})
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
