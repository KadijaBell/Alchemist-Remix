from app.models import db, Post, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_posts():
    posts = [
        {
            'user_id': 1,
            'source_id':1,
            'title': 'Exploring the Universe',
            'content': 'A deep dive into the cosmos and beyond.',
            'content_type': 'text',
            'media': None,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        },
        {
            'user_id': 2,
            'source_id':1,
            'title': 'Morning Podcast',
            'content': 'Listen to the latest updates on current events.',
            'content_type': 'audio',
            'media': 'https://www.nytimes.com/column/the-daily',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        },
        {
            'user_id': 3,
            'source_id':1,
            'title': 'Nature Photography',
            'content': 'A gallery of stunning nature images.',
            'content_type': 'image',
            'media': 'https://unsplash.com/',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        },
        {
            'user_id': 1,
            'source_id':1,
            'title': 'Tech Trends 2025',
            'content': 'The latest trends in technology and innovation.',
            'content_type': 'text',
            'media': None,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        },
        {
            'user_id': 2,
            'source_id':1,
            'title': 'Meditation Podcast',
            'content': 'Guided meditations for a calmer mind.',
            'content_type': 'audio',
            'media': 'https://revisionisthistory.com/',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        },
    ]

    for post in posts:
        new_post = Post(
            user_id=post['user_id'],
            title=post['title'],
            content=post['content'],
            content_type=post['content_type'],
            source_id=post['source_id'],
            media=post['media'],
            created_at=post['created_at'],
            updated_at=post['updated_at']
        )


    db.session.add(new_post)
    db.session.commit()
    return posts

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
        db.session.commit()
