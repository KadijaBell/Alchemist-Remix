from datetime import datetime
from .db import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user = db.relationship('User', back_populates='posts')
    comments = db.relationship('Comment', back_populates='post')



    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user': self.user.to_dict(),
            'comments': [comment.to_dict() for comment in self.comments]
        }

    def __repr__(self):
        return f'Post(id={self.id}, user_id={self.user_id}, content={self.content}, created_at={self.created_at}, updated_at={self.updated_at})'
