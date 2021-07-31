from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class PollutantUploadForm(FlaskForm):
    submit = SubmitField('Upload')
    photo = FileField("Photo", validators=[FileRequired(), FileAllowed('csv',
                                                                       "CSV Only!")])
