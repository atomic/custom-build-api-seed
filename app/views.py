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
                           title='Home',
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


@app.route('/iama/', methods=['GET'])
def get_posts():
    return jsonify({'posts': [post.get_url() for post in models.RedditThread.query.all()]})

# These are not views, but stuffs returned for certain request
@app.route('/iama/<id>/', methods=['GET'])
def get_post(id):
    return jsonify(models.RedditThread.query.get_or_404(id).export_data())

# For now disable user to POST to database
@app.route('/iama/', methods=['POST'])
def new_post():
    #post = post()
    #post.import_data(request.json)
    #db.session.add(post)
    #db.session.commit()
    #return jsonify({}), 201, {'Location': post.get_url()}
    return jsonify({}), 201, {'POST disabled'}

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
