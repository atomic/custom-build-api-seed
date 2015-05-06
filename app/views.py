# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Tony Lim <atomictheorist@gmail.com>
#
# Distributed under terms of the MIT license.

from app import app, models
from flask import render_template, flash, redirect, jsonify
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    # By here, all posts should already loaded to database
    mydatabase = models.RedditThread.query.all()
    return render_template("index.html",
                           title='Index',
                           posts=mydatabase)


# This is just for practice
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers= app.config['OPENID_PROVIDERS'])


@app.route('/comments', methods=['GET'])
@app.route('/mostcomments', methods=['GET'])
def mostcomments():
    myDB = models.RedditThread.query.order_by('num_comments desc').all()[:10]
    return  render_template('index.html',
                            title='Top 10 most commented post',
                            posts=myDB)

@app.route('/popular', methods=['GET'])
@app.route('/upvotes', methods=['GET'])
@app.route('/mostupvotes', methods=['GET'])
def mostupvotes():
    myDB = models.RedditThread.query.order_by('ups desc').all()[:10]
    return  render_template('index.html',
                            title='Top 10 most upvoted post',
                            posts=myDB)

@app.route('/controversial', methods=['GET'])
@app.route('/downvotes', methods=['GET'])
def mostdownvotes():
    myDB = models.RedditThread.query.order_by('ups asc').all()[:10]
    return  render_template('index.html',
                            title='Top 10 most downvoted post',
                            posts=myDB)

@app.route('/topauthor', methods=['GET'])
def topauthor():
    post_authors = models.RedditThread.query.order_by('author desc').all()
    all_author = filter(None, [p.author for p in post_authors])
    uniq_author = sorted(set(all_author))
    author_posttimes = zip(uniq_author, [all_author.count(uniq) for uniq in uniq_author])
    sorted_author_tupple = sorted(author_posttimes, key = lambda x: -x[1])
    return render_template('post_frequency.html',
                           title='Most and lest frequent Author post',
                           author_posts = sorted_author_tupple)


@app.route('/faq', methods=['GET'])
def faq():
    return render_template("faq.html", title='Faq')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Page not found.'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', title='Internal Server Error 500.'), 500

@app.route('/api/', methods=['GET'])
def get_posts():
    return jsonify({'posts': [post.get_url() for post in models.RedditThread.query.all()]})

# These are not views, but stuffs returned for certain request
@app.route('/api/<id>/', methods=['GET'])
def get_post(id):
    return jsonify(models.RedditThread.query.get_or_404(id).export_data())

# For now disable user to POST to database
@app.route('/api/', methods=['POST'])
def new_post():
    post = post()
    post.import_data(request.json)
    db.session.add(post)
    db.session.commit()
    return jsonify({}), 201, {'Location': post.get_url()}

@app.route('/iama/<int:id>', methods=['PUT'])
def edit_post(id):
    post = post.query.get_or_404(id)
    post.import_data(request.json)
    db.session.add(post)
    db.session.commit()
    return jsonify({}), 200

@app.route('/healthcheck', methods=['GET'])
def healthCheck():
    return jsonify()

