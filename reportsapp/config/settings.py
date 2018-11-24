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
    MONGO_URI = "mongodb://localhost:27017/development_db"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/testing_db"


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
