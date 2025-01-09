from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField, URLField
from wtforms.validators import DataRequired, Length, URL, Optional, ValidationError

class PostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(), Length(max=255)])
    content = TextAreaField("content", validators=[DataRequired()])
    content_type = SelectField(
        "content_type",
        choices=[
            ("Text", "Text"),
            ("Podcast", "Podcast"),
            ("Video", "Video"),
            ("Image", "Image"),
            ("Audio", "Audio"),
            ("Article", "Article"),
            ("Link", "Link"),
            ("Book", "Book"),
            ("Other", "Other"),
        ],
        validators=[DataRequired()],
    )
    media = FileField("media", validators=[Optional()])
    url = URLField("url", validators=[Optional(), URL()])


    def validate_content_type(form, field):
        valid_content_types = [
            "Text",
            "Podcast",
            "Video",
            "Image",
            "Audio",
            "Article",
            "Link",
            "Book",
            "Other",
        ]
        if field.data not in valid_content_types:
            raise ValidationError("Invalid content type.")
