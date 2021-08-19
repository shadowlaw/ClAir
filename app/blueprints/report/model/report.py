from app import db
from app.blueprints.report.model.report_detail import ReportDetail
from datetime import datetime


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("planning_application.id"))
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now)
    report_details = db.relationship("ReportDetail", backref="report", lazy=True)

    @staticmethod
    def get_reports(page=1, per_page=5):
        return Report.query.order_by(Report.created_on.desc()).paginate(page=page, per_page=per_page, error_out=False)
