from config import db
from ..common.models import TimeStampedBaseModel

__all__ = ['Checkup']


class Checkup(TimeStampedBaseModel):
    __tablename__ = 'checkup'
    id = db.Column(db.Integer(), primary_key=True)
    checkup_type = db.Column(db.String(120), nullable=False)
    checkup_report = db.Column(db.String(120), nullable=False)

    checkup_for_id = db.Column(db.ForeignKey("user.id"))
    checkup_for = db.relationship('User', backref='checkups')
    machine = db.Column(db.String(120), nullable=True)
    taken_by = db.Column(db.String(120), nullable=True)
    disease = db.Column(db.String(120), nullable=False)
