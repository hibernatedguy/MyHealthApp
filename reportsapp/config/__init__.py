from flask import Flask
from flask_pymongo import PyMongo

from .settings import config_by_name

mongo = PyMongo()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    mongo = PyMongo(app)
    return app
