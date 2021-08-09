from app import db
from enum import Enum


class TargetedPollutant(db.Model):
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), primary_key=True)
    tree_id = db.Column(db.String(255), db.ForeignKey('tree.id'), primary_key=True)
    targeted_pollutant_id = db.Column(db.String(255), db.ForeignKey('pollutant.id'), primary_key=True)
    target_type = db.Column(db.String(255))
    pollutant = db.relationship('Pollutant', lazy=True)
    tree_efficacy = None


class TargetedPollutantEnum(Enum):
    MAIN = 'PRIM'
    SECONDARY = 'SEC'
