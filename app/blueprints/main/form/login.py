from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Regexp


class Login(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Regexp(r'^[^!@#$%^&*()+\-=\[\]{};\':"\\|,.<>\/?]*$')])
    password = PasswordField("Password", validators = [InputRequired()])
    submit = SubmitField("Login")