from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length

class AccountManagementForm(FlaskForm):
    user_id = IntegerField("User ID", validators=[DataRequired()])
    platform = StringField(
        "Platform",
        validators=[
            DataRequired(),
            Length(max=50, message="Platform must be 50 characters or fewer.")
        ]
    )
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(max=100, message="Username must be 100 characters or fewer.")
        ]
    )
    settings = TextAreaField("Settings, (JSON)")
