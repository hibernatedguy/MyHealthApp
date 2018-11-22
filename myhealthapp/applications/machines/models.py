from config import db
from ..common.models import TimeStampedBaseModel

__all__ = ['Machine']


class Machine(TimeStampedBaseModel):
    __tablename__ = 'machine'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String, nullable=False)
    purchased_on = db.Column(db.DateTime, nullable=False)
