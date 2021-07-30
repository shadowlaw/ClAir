from app import db
from app.blueprints.report.model.report_detail import ReportDetail
from datetime import datetime


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("planning_application.id"), primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now)
    report_details = db.relationship("ReportDetail", backref="report", lazy=True)
