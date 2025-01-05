from app.models import db, Creative
from datetime import datetime

def seed_creatives():
    creative1 = Creative(
        title="New Blog Post",
        content="Tips for staying productive while working remotely.",
        content_type="Text",
        media=None,
        user_id=1,  # Assuming user with ID 1 exists
        schedule_id=1  # Assuming schedule with ID 1 exists
    )

    creative2 = Creative(
        title="Podcast Episode 1",
        content="Introducing our first podcast episode.",
        content_type="Audio",
        media="https://example.com/podcast-ep1.mp3",
        user_id=1,  # Assuming user with ID 1 exists
        schedule_id=2  # Assuming schedule with ID 2 exists
    )

    db.session.add_all([creative1, creative2])
    db.session.commit()

def undo_creatives():
    db.session.execute('DELETE FROM creatives;')
    db.session.commit()
