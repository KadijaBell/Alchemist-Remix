from app.models import db, User, schedule
from datetime import datetime
from sqlalchemy.sql import text


class Creative(db.Model):
    __tablename__ = 'creatives'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    media = db.Column(db.String(255), nullable=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedules.id'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    #Relations
    schedule = db.relationship('Schedule', back_populates='creatives')
    user = db.relationship('User', back_populates='creatives')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'content_type': self.content_type,
            'media': self.media,
            'schedule_id': self.schedule_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user_id': self.user_id
        }
