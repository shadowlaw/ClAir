from app import db


class PollutantLimitStatus(db.Model):

    id = db.Column(db.String(100), primary_key=True)
    description = db.Column(db.String(255), nullable=False)
