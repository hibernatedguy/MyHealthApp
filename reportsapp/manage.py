# import unittest

from flask_script import Manager
from flask_pymongo import PyMongo

# create environment
from config import create_app
from config.settings import secrets


# models registration
app = create_app(secrets.get('ENVIRONMENT', 'DEVELOPMENT'))
mongo = PyMongo(app)

# application URLs registration


# Manager Commands
manager = Manager(app)


@manager.command
def runserver():
    mydict = { "name": "John", "address": "Highway 37", "online": True}
    mongo.db.users.insert_one(mydict)
    online_users = mongo.db.users.find({"online": True})
    for x in online_users:
        print(x)
    app.run()


if __name__ == '__main__':
    manager.run()
