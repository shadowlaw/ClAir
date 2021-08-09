from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class AirQualityUploadForm(FlaskForm):
    submit = SubmitField('Confirm Upload')
    file = FileField("Select A File ", id='upload', validators=[FileRequired(message="Please select a file for upload"),
                                                                FileAllowed(['csv'], "Only CSV files are allowed")])
