from app import db
from app.blueprints.main.model.tree import Tree


class ReportDetail(db.Model):
    report_id = db.Column(db.Integer, db.ForeignKey("report.id"), primary_key=True)
    tree_id = db.Column(db.String(100), db.ForeignKey("tree.id"),  primary_key=True)
    quantity = db.Column(db.Integer)
    targeted_pollutant = db.Column(db.String(100), db.ForeignKey("pollutant.id"))
    pollutant = db.relationship('Pollutant', lazy=True)
