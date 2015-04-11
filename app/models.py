from app import db

class User(db.Model):
    id        = db.Column(db.Integer, primary_key = True)
    nickname  = db.Column(db.String(64), index    = True, unique   = True)
    email     = db.Column(db.String(120), index   = True, unique   = True)
    posts     = db.relationship('Post', backref   = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id        = db.Column(db.Integer, primary_key = True)
    body      = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class RedditThread(db.Model):
    id                      = db.Column(db.Integer, primary_key = True)
    author                  = db.Column(db.String(64), index = True, unique = True)
    name                    = db.Column(db.String(64), index = True)
    num_comments            = db.Column(db.Integer, index = True)
    domain                  = db.Column(db.String(16), index = True, nullable = True)
    subreddit_id            = db.Column(db.String(16), unique = True, nullable = True)
    score                   = db.Column(db.Integer, nullable = True)
    ups                     = db.Column(db.Integer, nullable = True)
    downs                   = db.Column(db.Integer, nullable = True)
    selftext                = db.Column(db.Text, nullable = True)
    link_flair_text         = db.Column(db.String(16), nullable = True)
    over_18                 = db.Column(db.String(5), nullable = True)
    thumbnail               = db.Column(db.String(16), nullable = True)
    edited                  = db.Column(db.Integer, nullable = True)
    link_flair_css_class    = db.Column(db.String(16), nullable = True)
    author_flair_css_class  = db.Column(db.String(16), nullable = True)
    is_self                 = db.Column(db.String(5), nullable = True)
    permalink               = db.Column(db.Text, nullable = True)
    url                     = db.Column(db.Text, nullable = True)
    title                   = db.Column(db.String(16), nullable = True)
    created_utc             = db.Column(db.Integer, nullable = True)
    distinguished           = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return '<Post : %r by %r' % (self.title, self.author)


