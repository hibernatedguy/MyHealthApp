from config import db
from ..common.models import TimeStampedBaseModel

__all__ = ['Disease', 'Checkup']


class Disease(TimeStampedBaseModel):
    __tablename__ = 'disease'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Checkup(TimeStampedBaseModel):
    __tablename__ = 'checkup'
    id = db.Column(db.Integer(), primary_key=True)
    checkup_type = db.Column(db.String(120), unique=True, nullable=False)
    checkup_report = db.Column(db.String(120), unique=True, nullable=False)

    checkup_for_id = db.Column(db.ForeignKey("user.id"))
    checkup_for = db.relationship('User', backref='checkups')

    machine_id = db.Column(db.ForeignKey("machine.id"))
    machine = db.relationship('Machine', backref='checkups')

    disease_id = db.Column(db.ForeignKey("disease.id"))
    disease = db.relationship('Disease', backref='checkups')
