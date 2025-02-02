from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, URL, Optional

class CreativeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    content = TextAreaField("Content", validators=[DataRequired()])
    content_type = SelectField(
        "Content Type",
        choices=[("Text", "Text"), ("Image", "Image"), ("Audio", "Audio")],
        validators=[DataRequired()],
    )
    media = URLField("Media", validators=[Optional(), URL()])
    schedule_id = IntegerField("Schedule ID", validators=[Optional()])
