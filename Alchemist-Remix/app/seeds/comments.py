from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text

def seed_comments():
    comments= [
        Comment(
            user_id=1,
            source_id=1,
            content='This article helped me understand the basics of transmutation.',
        ),
        Comment(
            user_id=2,
            source_id=2,
            content='Excellent writing! Looking forward to more content.',
        ),
        Comment(
            user_id=3,
            source_id=3,
            content='I have questions about the elixir preparation techniques mentioned.',
        ),
    ]

    for comment in comments:
        db.session.add(comment)
        db.session.commit()

    return comments

def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
