from app import db


class Town(db.Model):
    id = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    parish_id = db.Column(db.String(100), db.ForeignKey("parish.id"), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Numeric(precision=2), default=0)
    pollutants = db.relationship("TownPollutant", backref="town", lazy=True)
    permits = db.relationship("PlanningApplication", backref="town", lazy=True)
