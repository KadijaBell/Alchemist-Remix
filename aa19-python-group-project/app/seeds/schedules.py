from app.models import db, Schedule
from datetime import datetime, timedelta

def seed_schedules():
    schedule1 = Schedule(
        title="Morning Social Media Posts",
        description="Schedule for posting morning updates on social media",
        start_time=datetime.utcnow(),
        end_time=datetime.utcnow() + timedelta(hours=2),
        user_id=1  
    )

    schedule2 = Schedule(
        title="Weekly Podcast Release",
        description="Release schedule for weekly podcasts",
        start_time=datetime.utcnow() + timedelta(days=1),
        end_time=datetime.utcnow() + timedelta(days=1, hours=1),
        user_id=1
    )

    db.session.add_all([schedule1, schedule2])
    db.session.commit()

def undo_schedules():
    db.session.execute('DELETE FROM schedules;')
    db.session.commit()
