from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Reflection

class ReflectionForm(FlaskForm):



    content = StringField(
        "Content",
        validators=[
            DataRequired(message="Content is required."),
            Length(max=500, message="Content cannot exceed 500 characters."),
        ]
    )
    user_id = IntegerField(
        "User ID",
        validators=[DataRequired(message="User ID is required.")]
    )

    
