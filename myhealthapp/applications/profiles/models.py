from config import db
from ..common.models import TimeStampedBaseModel

__all__ = ['User']

diseases = db.Table('diseases',
                    db.Column('disease_id', db.Integer, db.ForeignKey('disease.id'), primary_key=True),
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
                    )


class User(TimeStampedBaseModel):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
