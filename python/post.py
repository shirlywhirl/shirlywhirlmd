#!/usr/bin/env python

from jinja2 import Template

class Post(object):
    post_template = Template("""
---
title: {{ title }}
author: Shirlene Obuobi
categories: {{ categories }}
tags: {{ tags }}
toc: false
---
{{ content }}
""")

    def __init__(ig_post):
        self.data = ig_post
        self.html = None

    def set_html(html):
        self.html = html

    def get_html():
        return self.html

    def get_tags():
        # Could it be denser? Probably
        return [word[1::].lower() for word in self.data.caption.split() if '#' in word]

    def get_categories():
        year = self.data.timestamp[:4:]
        if year in ['2020', '2019', '2018']:
            return "Residency"
        else:
            return "Medical School"

    def write_jekyll_post():
        if not self.html:
            print("Error, writing content before grabbing")
            return
        filename = "/mnt/src/shirlywhirlmd/_posts/" + self.get_title() + '-' + self.get_title()
        with open(filename, 'w') as post:
            post.write(post_template.render(title=self.get_title(),
                                            categories=self.get_categories(),
                                            tags=self.get_tags(),
                                            content=self.get_html()))

    def get_title():
        # TODO: Make this smart and fix above
        return self.data.timestamp[:10:]
