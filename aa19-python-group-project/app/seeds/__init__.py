from flask.cli import AppGroup
from .users import seed_users, undo_users
from .content_sources import seed_content_sources, undo_content_sources
from .comments import seed_comments, undo_comments
from .reflections import seed_reflections, undo_reflections
from .creative import seed_creatives, undo_creatives
from .schedules import seed_schedules, undo_schedules
from .post import seed_posts, undo_posts
from .account_management import seed_accounts, undo_accounts

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_content_sources()
        undo_comments()
        undo_reflections()
        undo_creatives()
        undo_schedules()
        undo_posts()
        undo_accounts()
    seed_users()
    seed_content_sources()
    seed_comments()
    seed_reflections()
    seed_creatives()
    seed_schedules()
    seed_posts()
    seed_accounts()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_content_sources()
    undo_comments()
    undo_reflections()
    undo_comments()
    undo_content_sources()
    undo_reflections()
    undo_creatives()
    undo_schedules()
    undo_posts()
    undo_accounts()


    # Add other undo functions here
