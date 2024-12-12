from app.models import db, ContentSource, environment, SCHEMA
from sqlalchemy.sql import text


def seed_content_sources():
    content_sources = [
        {
            'name': 'The New York Times',
            'source_type': 'Newspaper',
            'url': 'https://www.nytimes.com/'
        },
        {
            'name': 'The Washington Post',
            'source_type': 'Newspaper',
            'url': 'https://www.washingtonpost.com/'
        },
        {
            'name': 'The Guardian',
            'source_type': 'Newspaper',
            'url': 'https://www.theguardian.com/'
        },
        {
            'name': 'Alchemy Journal',
            'source_type': 'Journal',
            'url': 'http://alchemyjournal.com'
        },
        {
            'name': 'Fusion Weekly',
            'source_type': 'Magazine',
            'url': 'http://fusionweekly.com'
        },
        {
            'name': 'Elixir Recipes',
            'source_type': 'Blog',
            'url': 'http://elixirrecipes.com'
        },
        {
            'name': 'CR JAY Blog',
            'source_type': 'Video',
            'url': 'https://youtu.be/DvBOZHIFFq8?si=-Qxa67gFPg6RCxbB'
        }
    ]

    for source in content_sources:
        new_source = ContentSource(
            name=source['name'],
            source_type=source['source_type'],
            url=source['url']
        )
        db.session.add(new_source)

    db.session.commit()

    return content_sources


def undo_content_sources():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.content_sources RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM content_sources"))

    db.session.commit()
