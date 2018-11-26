from flask.views import MethodView
from flask import jsonify, request

from config import db

from ..profiles.models import User
from .models import *
from .serializers import *

__all__ = ['UserCheckupMethodView', 'BulkCheckupReportMethodView']


class UserCheckupMethodView(MethodView):
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
        # support multiple checkup reports and single report

        # multiple report
        if isinstance(data, list):
            for checkup in data:

                # putting user query here to reuse the whole CheckupMethodView for bulk create.
                user = User.query.filter_by(username=checkup.get('checkup_for')).first()

                if not user:
                    return jsonify({'details': 'User does not exist!'}), 404

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
            # putting user query here to reuse the whole CheckupMethodView for bulk create.
            user = User.query.filter_by(username=data.get('checkup_for')).first()

            if not user:
                return jsonify({'details': 'User does not exist!'}), 404

            # putting user query here to reuse the whole CheckupMethodView for bulk create.
            _checkup = Checkup(checkup_type=data.get('checkup_type'),
                               checkup_report=data.get('checkup_report'),
                               machine=data.get('machine'),
                               taken_by=data.get('taken_by'),
                               disease=data.get('disease'))
            _checkup.checkup_for = user
            db.session.add(_checkup)
            db.session.commit()
        return jsonify({'details': 'User checkup created'}), 201

    def delete(self, current_user, username=None, checkup_id=None):
        user = User.query.filter_by(username=username).first()
        checkup = Checkup.query.filter_by(checkup_for=user, id=checkup_id).first()
        if checkup:
            db.session.delete(checkup)
            db.session.commit()
            return jsonify({'details': 'Checkup report deleted'}), 204
        return jsonify({'details': 'Checkup report does not exist.'}), 404


class BulkCheckupReportMethodView(MethodView):
    checkups_serializer = CheckupsSerializer

    def get(self, current_user):
        '''
        1. fetch signle user if username exists else return all users
        2. if username provided in url-param return user-detail else return 404-DoesNotExists
        '''
        checkups = Checkup.query.all()
        if not checkups:
            return jsonify({'details': 'Checkup does not exist.'}), 404
        output = self.checkups_serializer.dump(checkups).data
        return jsonify(output), 200

    def post(self, current_user):
        data = request.get_json()
        # support multiple checkup reports and single report
        # multiple report
        if isinstance(data, list):
            for checkup in data:

                # putting user query here to reuse the whole CheckupMethodView for bulk create.
                user = User.query.filter_by(username=checkup.get('checkup_for')).first()

                if not user:
                    return jsonify({'details': 'User does not exist!'}), 404

                _checkup = Checkup(checkup_type=checkup.get('checkup_type'),
                                   checkup_report=checkup.get('checkup_report'),
                                   machine=checkup.get('machine'),
                                   taken_by=checkup.get('taken_by'),
                                   disease=checkup.get('disease'))
                _checkup.checkup_for = user
                db.session.add(_checkup)
                db.session.commit()
                return jsonify({'details': 'User checkup created'}), 201

        # single data
        if isinstance(data, dict):
            # putting user query here to reuse the whole CheckupMethodView for bulk create.
            user = User.query.filter_by(username=data.get('checkup_for')).first()

            if not user:
                return jsonify({'details': 'User does not exist!'}), 404

            # putting user query here to reuse the whole CheckupMethodView for bulk create.
            _checkup = Checkup(checkup_type=data.get('checkup_type'),
                               checkup_report=data.get('checkup_report'),
                               machine=data.get('machine'),
                               taken_by=data.get('taken_by'),
                               disease=data.get('disease'))
            _checkup.checkup_for = user
            db.session.add(_checkup)
            db.session.commit()
            return jsonify({'details': 'User checkup created'}), 201        
        return jsonify({'details': 'Bad request.'}), 400
