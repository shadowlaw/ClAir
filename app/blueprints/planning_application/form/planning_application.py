from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField
from wtforms.validators import InputRequired, DataRequired, Regexp, NumberRange
from app.constants import CONSTANTS


class PlanningApplicationForm(FlaskForm):
    parish = SelectField("Parish", validators=[InputRequired()])
    town = SelectField("Town", choices=[], validators=[InputRequired()])
    area_name = StringField("Area Name", validators=[InputRequired(), Regexp(r'^[^!@#$%^&*()+\-=\[\]{};\':"\\|,.<>\/?]*$')])
    square_footage = DecimalField("Square Footage", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    AQI = DecimalField("AQI", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"]),
                                          NumberRange(min=0, max=500, message="Please enter a number between 0 and 500")])
    PM25 = DecimalField("PM 2.5", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    PM10 = DecimalField("PM 10", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    CO = DecimalField("CO", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    NO2 = DecimalField("NO2", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    SO2 = DecimalField("SO2", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    O3 = DecimalField("O3", validators=[InputRequired(), DataRequired(message=CONSTANTS["NUMBER_REQUIRED_VALIDATOR_MESSAGE"])])
    submit = SubmitField("Submit Request")
