from app.models import db, Reflection, environment,SCHEMA
from sqlalchemy.sql import text


def seed_reflections():
    reflections = [
        Reflection(
            user_id=1,
            source_id=1,
            content='This source is fantastic for beginners in alchemy.',
        ),
        Reflection(
            user_id=2,
            source_id=2,
            content='A great collection of advanced alchemical techniques.',
        ),
        Reflection(
            user_id=3,
            source_id=3,
            content='Very inspiring content on modern alchemy practices.',
        ),
    ]

    for reflection in reflections:
        db.session.add(reflection)
        db.session.commit()

    return reflections


def undo_reflections():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reflections RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reflections"))

    db.session.commit()
