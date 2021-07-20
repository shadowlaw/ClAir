from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permits_created = db.relationship("Permit", backref="user", lazy=True)
