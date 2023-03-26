from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

# from db import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "username_label",
        validators=[
            InputRequired(message="Username required"),
            Length(
                min=4, max=25, message="Username must be between 4 and 25 characters"
            ),
        ],
    )
    password = PasswordField(
        "password_label",
        validators=[
            InputRequired(message="Password required"),
            Length(
                min=4, max=25, message="Password must be between 4 and 25 characters"
            ),
        ],
    )
    confirm_pswd = PasswordField(
        "confirm_pswd_label",
        validators=[
            InputRequired(message="Password required"),
            EqualTo("password", message="Password must match"),
        ],
    )
    submit_button = SubmitField("Create")

    '''def validate_username(self, username):
        user_obj = User.query.filter_by(username=username.data).first()
        if user_obj:
            raise ValidationError("Username already exists. Select different username")'''
