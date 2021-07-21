from app import db


class PermitAreaPollutant(db.Model):
    permit_id = db.Column(db.String(100), db.ForeignKey("permit.id"), primary_key=True)
    pollutant_id = db.Column(db.String(100), db.ForeignKey("pollutant.id"), primary_key=True)
    pollutant_level = db.Column(db.Numeric(precision=2), nullable=False)
