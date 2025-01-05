from app.models import db
from datetime import datetime

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    platform = db.Column(db.String(50), nullable=False)  # e.g., Twitter, Facebook
    username = db.Column(db.String(100), nullable=False)
    settings = db.Column(db.JSON, nullable=True)  # JSON field for storing custom settings
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = db.relationship('User', back_populates='accounts')

    # To dict method for easy serialization
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'platform': self.platform,
            'username': self.username,
            'settings': self.settings,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
