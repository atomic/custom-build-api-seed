# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Tony Lim <atomictheorist@gmail.com>
#
# Distributed under terms of the MIT license.

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models