from flask import Flask
from flask_pymongo import PyMongo

from .settings import config_by_name
from config.settings import secrets


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    return app


def get_app_and_db(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    mongo = PyMongo(app)
    return app, mongo


app_info, monod_db = get_app_and_db(secrets.get('ENVIRONMENT', 'DEVELOPMENT'))
