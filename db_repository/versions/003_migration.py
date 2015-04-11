from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reddit_thread = Table('reddit_thread', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('author', String(length=64)),
    Column('name', String(length=64)),
    Column('num_comments', Integer),
    Column('domain', String(length=16)),
    Column('subreddit_id', String(length=16)),
    Column('score', Integer),
    Column('ups', Integer),
    Column('downs', Integer),
    Column('selftext', Text),
    Column('link_flair_text', String(length=16)),
    Column('over_18', String(length=5)),
    Column('thumbnail', String(length=16)),
    Column('edited', Integer),
    Column('link_flair_css_class', String(length=16)),
    Column('author_flair_css_class', String(length=16)),
    Column('is_self', String(length=5)),
    Column('permalink', Text),
    Column('url', Text),
    Column('title', String(length=16)),
    Column('created_utc', Integer),
    Column('distinguished', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['reddit_thread'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['reddit_thread'].drop()
