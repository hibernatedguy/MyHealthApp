import requests

from config.flask_celery import make_celery
from config import create_app
from config.settings import secrets

app = create_app(secrets.get('ENVIRONMENT'))
celery = make_celery(app)


@celery.task(name='process_delete_redemption')
def task_delete_redemption(red_id):
    r = requests.get('http://127.0.0.1:8080/users/')
    print(r.status_code, r.text)


# task_delete_redemption.delay(20)
