import os
import json

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


# READ SECREJSON FILE
SECRETS_FILE = os.path.abspath('config/secrets.json')

if os.path.exists(SECRETS_FILE) is False:
    raise Exception(" Please add 'secrets.json' file in config/ folder.")

with open(SECRETS_FILE) as f:
    secrets = json.loads(f.read())


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'development_sqlite.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/development_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testing_db')
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/testing_db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    DEVELOPMENT=DevelopmentConfig,
    TESTING=TestingConfig,
    PRODUCTION=ProductionConfig
)

key = Config.SECRET_KEY
