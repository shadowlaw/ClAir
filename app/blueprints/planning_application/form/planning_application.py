from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField
from wtforms.validators import InputRequired, DataRequired, Regexp, NumberRange
from app.constants import CONSTANTS
from flask import Markup


class PlanningApplicationForm(FlaskForm):
    parish = SelectField("Parish", validators=[InputRequired()])
    town = SelectField("Town", choices=[], validators=[InputRequired()])
    folio_number = StringField("Folio Number",
                               validators=[
                                    InputRequired(),
                                    DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"]),
                                    Regexp(r'^[0-9]{3}$', message='Please enter a valid Folio Number. 001-999')
                               ])
    area_name = StringField("Area Name", validators=[InputRequired(), Regexp(r'^[^!@#$%^&*()+\-=\[\]{};\':"\\|,.<>\/?]*$')])
    square_footage = DecimalField("Square Footage", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    AQI = DecimalField("AQI", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"]),
                                          NumberRange(min=0, max=500, message="Please enter a number between 0 and 500")])
    PM25 = DecimalField(Markup("PM<sub>2.5</sub>"), id='PM25', validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    PM10 = DecimalField(Markup("PM<sub>10</sub>"), id='PM10', validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    CO = DecimalField("CO", id='CO', validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    NO2 = DecimalField(Markup("NO<sub>2</sub>"), id='NO2', validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    SO2 = DecimalField(Markup("SO<sub>2</sub>"), id='SO2', validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    O3 = DecimalField(Markup("O<sub>3</sub>"), id='O3', validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    submit = SubmitField("Submit Request")
