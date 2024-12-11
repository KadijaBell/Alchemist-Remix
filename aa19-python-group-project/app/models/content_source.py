# This model creates a table with fields for managing content sources. The to_dict method makes it easier to convert the database records into JSON for API responses.

from app.models import db
from datetime import datetime

class ContentSource(db.Model):
    __tablename__ = 'content_sources'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    source_type = db.Column(db.String(255), nullable=False)
    url= db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    glances = db.Column(db.Integer, default=0)
    elixirs = db.Column(db.Integer, default=0)
    weighted_elixirs = db.Column(db.Float, default=0.0)
    transmutations = db.Column(db.Integer, default=0)



    comments = db.relationship('Comment', back_populates='source', cascade="all, delete-orphan")
    reflections = db.relationship('Reflection', back_populates='source', cascade="all, delete-orphan")
    


    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "media_type": self.source_type,
            "url": self.url,
            "created_at": self.created_at,
            "updated_at": self.updated_at

        }
