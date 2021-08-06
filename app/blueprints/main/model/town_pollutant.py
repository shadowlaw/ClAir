from sqlalchemy import PrimaryKeyConstraint

from app import db
from datetime import datetime


class TownPollutant(db.Model):
    town_id = db.Column(db.String(100), db.ForeignKey("town.id"), primary_key=True)
    pollutant_id = db.Column(db.String(100), db.ForeignKey("pollutant.id"), primary_key=True)
    pollutant_level = db.Column(db.Numeric(precision=2), nullable=False)
    collection_date = db.Column(db.DateTime, default=datetime.now, primary_key=True)
