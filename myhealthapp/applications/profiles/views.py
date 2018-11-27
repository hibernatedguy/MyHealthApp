from flask.views import MethodView
from flask import jsonify, request

from config import db

from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

from .models import *
from .serializers import *

__all__ = ['UserMethodView']


class UserMethodView(MethodView):
    single_user_serializer = UserSerializer
    users_serializer = UsersSerializer

    def get(self, username=None, current_user=None):
        '''
        1. fetch signle user if username exists else return all users
        2. if username provided in url-param return user-detail else return 404-DoesNotExists
        '''
        if username:
            user = User.query.filter_by(username=username).first()
            if not user:
                return jsonify({'details': '{} Does not Exists'.format(username)}), 404
            output = self.single_user_serializer.dump(user).data
            return jsonify(output), 200
        user = User.query.all()
        output = self.users_serializer.dump(user).data
        return jsonify(output), 200

    def post(self, current_user=None):
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

    def delete(self, username=None, current_user=None, ):
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'details': '{} Deleted'.format(username)}), 204
        return jsonify({'details': '{} Does not Exists'.format(username)}), 404

    def put(self, username, current_user=None):
        # delete a single user
        user = User.query.filter_by(username=username).first()
        try:
            if user is not None:
                data = request.get_json()
                for key, value in data.items():
                    if key is not None:
                        setattr(user, key, value)

                # hash password if provided.
                if 'password' in data.keys():
                    user.password = generate_password_hash(data.get('password'))
                db.session.commit()
                return jsonify({'details': '{} Patched'.format(username)}), 200
            return jsonify({'details': '{} Does Not Exists'.format(username)}), 404
        except IntegrityError:
            return jsonify({'details': 'User with same information is already exists.'}), 400
