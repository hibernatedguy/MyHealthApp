from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .settings import config_by_name

# from celery import Celery
# from config.settings import secrets

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


# def create_app_with_celery(config_name):
#     app = create_app(secrets.get('ENVIRONMENT'))
#     celery = make_celery(app)

#     from celery import current_app
#     from celery.bin import worker

#     application = current_app._get_current_object()
#     worker = worker.worker(app=application)
#     options = {
#         'broker': app.config['CELERY_BROKER_URL'],
#         'loglevel': 'INFO',
#         'traceback': True,
#     }
#     worker.run(**options)
#     return app, celery
