from flask.views import MethodView
from flask import jsonify, request

from config import db

from sqlalchemy.exc import IntegrityError

from ..profiles.models import User
from .models import *
from .serializers import *

__all__ = ['CheckupMethodView']


class CheckupMethodView(MethodView):
    single_checkup_serializer = CheckupSerializer
    checkups_serializer = CheckupsSerializer

    def get(self, current_user, username=None):
        '''
        1. fetch signle user if username exists else return all users
        2. if username provided in url-param return user-detail else return 404-DoesNotExists
        '''
        if username:
            user = User.query.filter_by(username=username).first()
            if not user:
                return jsonify({'details': 'Checkup does not exists for {}'.format(username)}), 404
            output = self.checkups_serializer.dump(user.checkups).data
            return jsonify(output), 200

    def post(self, current_user, username=None):
        data = request.get_json()
        user = User.query.filter_by(username=username).first()
        if not username:
            return jsonify({'details': 'User does not exist!'.format(username)}), 404

        # support multiple checkup reports and single report

        # multiple report
        if isinstance(data, list):
            for checkup in data:
                _checkup = Checkup(checkup_type=checkup.get('checkup_type'),
                                   checkup_report=checkup.get('checkup_report'),
                                   machine=checkup.get('machine'),
                                   taken_by=checkup.get('taken_by'),
                                   disease=checkup.get('disease'))
                _checkup.checkup_for = user
                db.session.add(_checkup)
                db.session.commit()

        # single data
        if isinstance(data, dict):
            _checkup = Checkup(checkup_type=data.get('checkup_type'),
                               checkup_report=data.get('checkup_report'),
                               machine=data.get('machine'),
                               taken_by=data.get('taken_by'),
                               disease=data.get('disease'))
            _checkup.checkup_for = user
            db.session.add(_checkup)
            db.session.commit()
        return jsonify({'details': 'User checkup created'}), 201

    def delete(self, current_user, username):
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'details': '{} Deleted'.format(username)}), 204
        return jsonify({'details': '{} Does not Exists'.format(username)}), 404

    def put(self, current_user, username):
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
