import datetime as dt
from .db import db




class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=True)
    source_id = db.Column(db.Integer, db.ForeignKey('content_sources.id'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    user = db.relationship('User', back_populates='comments')
    post = db.relationship('Post', back_populates='comments',foreign_keys=[post_id])
    source = db.relationship('ContentSource', back_populates='comments', foreign_keys=[source_id])

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'source_id': self.source_id,
            'created_at': self.created_at
        }

    def __repr__(self):
        return (f"Comment(id={self.id}, content={self.content[:30]}, user_id={self.user_id}, "
                f"post_id={self.post_id}, source_id={self.source_id}, created_at={self.created_at})")
