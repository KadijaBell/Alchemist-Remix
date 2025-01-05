from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

class ScheduleForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    description = TextAreaField("Description", validators=[Length(max=1000), DataRequired()])
    start_time = DateTimeField("Start Time", format="%Y-%m-%dT%H:%M:%S", validators=[DataRequired()])
    end_time = DateTimeField("End Time", format="%Y-%m-%dT%H:%M:%S", validators=[DataRequired()])

    def validate_end_time(form, field):
        if field.data <= form.start_time.data:
            raise ValidationError("End time must be after start time.")
