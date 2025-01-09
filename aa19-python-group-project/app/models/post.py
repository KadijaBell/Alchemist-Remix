from datetime import datetime
from .db import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    media = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255), nullable=True)
    source_id = db.Column(db.Integer, db.ForeignKey('content_sources.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    #realtions
    user = db.relationship('User', back_populates='posts')
    comments = db.relationship('Comment', back_populates='post')
    content_source = db.relationship("ContentSource", back_populates='posts')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'content': self.content,
            'content_type': self.content_type,
            'media': self.media,
            'url': self.url,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user': self.user.to_dict(),
            'comments': [comment.to_dict() for comment in self.comments],
            'source_id': self.feed_id
        }
