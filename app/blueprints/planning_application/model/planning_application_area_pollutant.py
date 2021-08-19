from app import db
from app.blueprints.planning_application.model.pollutant_limit_status import PollutantLimitStatus


class PlanningApplicationAreaPollutant(db.Model):
    application_id = db.Column(db.Integer(), db.ForeignKey("planning_application.id"), primary_key=True)
    pollutant_id = db.Column(db.String(100), db.ForeignKey("pollutant.id"), primary_key=True)
    pollutant_level = db.Column(db.Numeric(precision=2), nullable=False)
    status_id = db.Column(db.String(100), db.ForeignKey('pollutant_limit_status.id'))
    pollutant = db.relationship('Pollutant', lazy=True)
    status = db.relationship('PollutantLimitStatus', lazy=True)
