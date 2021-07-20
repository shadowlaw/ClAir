from app import db


class Parish(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    towns = db.relationship("Town", backref="parish", lazy=True)
