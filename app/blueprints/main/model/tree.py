from app import db
from app.blueprints.main.model.tree_type import TreeType


class Tree(db.Model):

    id = db.Column(db.String(100),  primary_key=True)
    name = db.Column(db.String(255),  nullable=False)
    type_id = db.Column(db.String(100), db.ForeignKey('tree_type.id'))
    maturity_size = db.Column(db.Numeric(), nullable=False)
    age_to_maturity = db.Column(db.Numeric(), nullable=True)
    space_required = db.Column(db.Numeric(), nullable=False)
    img_name = db.Column(db.String(100), default='default_tree.jpeg')
    type = db.relationship('TreeType', backref='trees', lazy=True)
    report_details = db.relationship("ReportDetail", backref="tree", lazy=True)
