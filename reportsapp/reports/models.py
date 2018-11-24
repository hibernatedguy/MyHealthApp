from config import mongo_db as db
from flask_mongoalchemy import BaseQuery

__all__ = ['User', 'Checkup']


class UserQuerySet(BaseQuery):

    def get_users(self, username):
        return self.filter(self.type.username == username).all()

    def get_user(self, username):
        return self.filter(self.type.username == username)

    def get_checkups(self, username):
        return Checkup.query.filter(Checkup.checkup_for.username == username).all()


class User(db.Document):
    query_class = UserQuerySet
    username = db.StringField()


class Checkup(db.Document):
    disease = db.StringField()
    machine = db.StringField()
    taken_by = db.StringField()
    created_at = db.StringField()
    checkup_for = db.DocumentField(User)
