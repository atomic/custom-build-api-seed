# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Tony Lim <atomictheorist@gmail.com>
#
# Distributed under terms of the MIT license.

from app import db, models, views
import json
import os.path

file = open('reddit_IamA.json')
ListOfJson = json.load(file)

# clear database
RThread = models.RedditThread.query.all()
for th in RThread:
    db.session.delete(th)
db.session.commit()

# now fill the database
# u = models.RedditThread(id = list_json[0][])
for json_item in ListOfJson:
    db.session.add(models.RedditThread(
        # id(json_item['id']),
        author                   =( json_item['author']),
        name                     =( json_item['name']),
        num_comments             =( json_item['num_comments']),
        domain                   =( json_item['domain']),
        subreddit_id             =( json_item['subreddit_id']),
        score                    =( json_item['score']),
        ups                      =( json_item['ups']),
        downs                    =( json_item['downs']),
        selftext                 =( json_item['selftext']),
        link_flair_text          =( json_item['link_flair_text']),
        over_18                  =( json_item['over_18']),
        thumbnail                =( json_item['thumbnail']),
        edited                   =( json_item['edited']),
        link_flair_css_class     =( json_item['link_flair_css_class']),
        author_flair_css_class   =( json_item['author_flair_css_class']),
        is_self                  =( json_item['is_self']),
        permalink                =( json_item['permalink']),
        url                      =( json_item['url']),
        title                    =( json_item['title']),
        created_utc              =( json_item['created_utc']),
        distinguished            =( json_item['distinguished'])))

db.session.commit()
