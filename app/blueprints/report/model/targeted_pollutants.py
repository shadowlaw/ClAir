from app import db
from enum import Enum

class TargetedPollutant(db.Model):
    report_id = db.Column(db.Integer, primary_key = True)
    tree_id = db.Column(db.String(255), primary_key = True)
    targeted_pollutant_id = db.Column(db.String(255), primary_key = True)
    target_type = db.Column(db.String(255))

class TargetedPollutantEnum(Enum):
    MAIN = 'PRIM'
    SECONDARY = 'SEC'