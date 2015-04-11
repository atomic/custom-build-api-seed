# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Tony Lim <atomictheorist@gmail.com>
#
# Distributed under terms of the MIT license.

from app import app, models
from flask import render_template, flash, redirect
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

#@app.route('/healthCheck', methods=['GET'])
#def healthCheck():
    #return jsonify(VKk)
