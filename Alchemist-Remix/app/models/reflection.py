from datetime import datetime
from .db import db


class Reflection(db.Model):
    __tablename__ = 'reflections'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('content_sources.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', back_populates='reflections')
    source = db.relationship('ContentSource', back_populates='reflections')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'source_id': self.source_id,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
