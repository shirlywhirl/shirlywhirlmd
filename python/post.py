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

    def __init__(self, ig_post, html):
        self.data = ig_post
        self.html = html

    def get_tags(self):
        # Could it be denser? Probably
        if not self.data.caption:
            return []
        return sorted([word[1::].lower() for word in self.data.caption.split() if '#' in word])

    def get_categories(self):
        year = self.data.timestamp[:4:]
        if year in ['2020', '2019', '2018']:
            return "Residency"
        else:
            return "Medical School"

    def write_jekyll_post(self):
        filename = "/mnt/src/shirlywhirlmd/_posts/" + self.get_title() + '-' + self.get_title() + ".md"
        with open(filename, 'w') as post:
            post.write(Post.post_template.render(title=self.get_title(),
                                            categories=self.get_categories(),
                                            tags=self.get_tags(),
                                            content=self.html))

    def get_title(self):
        # TODO: Make this smart and fix above
        return self.data.timestamp[:10:]
