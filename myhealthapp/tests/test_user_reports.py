from config import db

import json
from utils.random_hex import key_gen
from applications.profiles.models import User
from applications.checkups.models import Checkup

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

random_user_data = {'username': 'pardus{}'.format(key_gen())}


def test_create_user(test_client):
    # save user
    user = User(username=random_user_data.get('username'), password=random_user_data.get('password'))
    db.session.add(user)
    db.session.commit()

    # check if user created or not?
    fetched_user = User.query.filter_by(username=random_user_data.get('username')).first()
    assert fetched_user.username == random_user_data.get('username')


def test_create_checkup(test_client):
    checkup_data = {
        "checkup_type": "BLOOD PRESSURE",
        "checkup_report": "ALL FINE. 20.90",
        "checkup_for": "{}".format(random_user_data.get('username')),
        "machine": "BP PRESSURE CHECK MACH",
        "taken_by": "Ayush",
        "disease": "BP"
    }
    # save checkup information
    fetched_user = User.query.filter_by(username=random_user_data.get('username')).first()
    checkup = Checkup(
        checkup_type=checkup_data.get('checkup_data'),
        checkup_report=checkup_data.get("checkup_report"),
        checkup_for=fetched_user, machine=checkup_data.get('machine'),
        taken_by=checkup_data.get('taken_by'))
    db.session.add(checkup)
    db.session.commit()

    # check if user created or not?
    checkup_query = Checkup.query.filter(check_for=fetched_user)
    checkup_query_last_item = checkup_query.order_by(Checkup.id.desc()).first()
    assert checkup_query_last_item.username == random_user_data.get('username')
    assert checkup_query_last_item.checkup_type == checkup_data.get('checkup_type')
