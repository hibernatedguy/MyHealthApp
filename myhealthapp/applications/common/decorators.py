import jwt
from functools import wraps

from flask import jsonify, request

from config.settings import secrets
from ..profiles.models import User


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'details': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, secrets.get('SECRET_KEY'))
            current_user = User.query.filter_by(username=data.get('username')).first()
        except Exception as e:
            return jsonify({'detail': 'Token is invalid!'})

        return f(current_user, *args, **kwargs)
    return decorated
