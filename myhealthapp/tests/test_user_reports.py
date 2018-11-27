from config import db
from applications.profiles.models import User
from applications.checkups.models import Checkup

from .generate_hex import key_gen

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

random_user_data = {'username': 'pardus{}'.format(key_gen()), 'password': 'password'}


def test_create_user(test_client):
    # save user
    user = User(username=random_user_data.get('username'), password=random_user_data.get('password'))
    db.session.add(user)
    db.session.commit()

    # check if user created or not?
    fetched_user = User.query.filter_by(username=random_user_data.get('username')).first()
    assert fetched_user.username == random_user_data.get('username')


def test_create_checkup(test_client):

    # save checkup information
    fetched_user = User.query.filter_by(username=random_user_data.get('username')).first()
    checkup = Checkup(
        checkup_type="BLOOD PRESSURE",
        checkup_report="ALL FINE. 20.90",
        checkup_for=fetched_user, machine="BP PRESSURE CHECK MACH",
        taken_by="Ayush",
        disease="DIA")
    db.session.add(checkup)
    db.session.commit()
    # check if user created or not?
    checkup_query = Checkup.query.all()
    checkup_query_last_item = checkup_query[-1]
    assert checkup_query_last_item.checkup_for.username == random_user_data.get('username')
    assert checkup_query_last_item.checkup_type == "BLOOD PRESSURE"
