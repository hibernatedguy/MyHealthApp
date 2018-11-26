from flask import jsonify
import requests
import json
# from flask import Flask

from celery.decorators import periodic_task
from datetime import timedelta

from config.flask_celery import make_celery
from config import create_app
from config.settings import secrets, REPORT_SERVER_URL
# from flask_sqlalchemy import SQLAlchemy

from applications.checkups.models import Checkup
from applications.checkups.serializers import CheckupsSerializer


app = create_app(secrets.get('ENVIRONMENT'))

celery = make_celery(app)


def get_last_sync_id():
    with open('checkup_log.json') as log_file:
        data = json.load(log_file)
    return data.get('last_log')


def set_new_sync_id(checkup_id):
    data = {'last_log': checkup_id}
    with open('checkup_log.json', 'w') as outfile:
        json.dump(data, outfile)


@periodic_task(run_every=timedelta(seconds=5))
def send_reports_to_report_server():

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    last_id = get_last_sync_id()
    checkup_query = Checkup.query.filter(Checkup.id > last_id)
    data = CheckupsSerializer.dump(checkup_query).data
    checkup_query_last_item = checkup_query.order_by(Checkup.id.desc()).first()
    if checkup_query_last_item:
        r = requests.post(REPORT_SERVER_URL, data=json.dumps(data), headers=headers)
        # set new sync id
        set_new_sync_id(checkup_query_last_item.id)
        # show report information
        print(r.status_code, r.text)
    return True