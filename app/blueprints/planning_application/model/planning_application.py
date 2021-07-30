from app import db
from datetime import datetime
from app.blueprints.report.model.report import Report


class PlanningApplication(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(100), nullable=False)
    square_footage = db.Column(db.Numeric(precision=2))
    town_id = db.Column(db.String(100), db.ForeignKey("town.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_on = db.Column(db.DateTime, nullable=True, default=datetime.now)
    pollutants = db.relationship("PlanningApplicationAreaPollutant", backref="planning_application", lazy=True)
    report = db.relationship("Report", backref="planning_application", lazy=True)
