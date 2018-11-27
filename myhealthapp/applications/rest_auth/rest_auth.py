import jwt
import datetime

from flask.views import MethodView
from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError

from config.settings import secrets
from config import db
from ..profiles.models import User


__all__ = ['RestAuthView']


class RestAuthView(MethodView):
    def get(self):
        auth = request.authorization
        if auth and auth.password and auth.username:
            user = User.query.filter_by(username=auth.username).first()

            if not user:
                return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

            if check_password_hash(user.password, auth.password):
                token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=300)},
                                   secrets.get('SECRET_KEY'))
                return jsonify({'token': token.decode('UTF-8')})
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    def post(self):
        '''
        CREATE new user
        '''
        try:
            data = request.get_json()
            hashed_password = generate_password_hash(data.get('password'))
            new_user = User(username=data.get('username'), password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'details': 'New user created'}), 201
        except IntegrityError:
            return jsonify({'details': 'User with same information is already exists.'}), 400
