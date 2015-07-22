#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gnupyx'
SITENAME = u'Gnupyx'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = "../pelican-cait"


#Cusom
USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('Blog', ''),
                    #('CV', 'pages/cv.html'),
                    ('Contact', 'pages/contact.html'))

CONTACT_EMAIL = "contact@gnupyx.fr"
CONTACTS = (('linkedin', 'https://www.linkedin.com/pub/j%C3%A9r%C3%A9my-barascut/22/107/446'),
            ('twitter', 'https://twitter.com/gnupyx'),
            ('github', 'https://github.com/jbarascut'),)


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
