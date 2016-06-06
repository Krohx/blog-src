#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from hashlib import md5



SITENAME = u'Blog | Krohx'
DESCRIPTION = u"Documentation is the soul of technology."
SITE_TAGLINE = DESCRIPTION
SITE_SOURCE = u'https://github.com/krohx/blog-src'

AUTHOR = u'Krohx'

# custom config variable for URLS
URLS = {
	'krohx' : ('http://krohx.github.io', 'this startup'),
	'niit' : ('http://www.niitlagos.com/about.html', 'NIIT'),
	}

# helper function to format URLs for BIO
def get_link(name):
	return '<a href="{url}">{url_title}</a>'.format(url=URLS.get(name, '')[0], url_title=URLS.get(name, '')[1])

BIO = \
	u'''
		<p>Krohx is a software company. We are committed to building digital solutions that help grow businesses and meet individual needs.
		</p>
	'''.format()



AUTHOR_SHORTBIO = u'Software Company'
AUTHOR_EMAIL = u'krohxinc@gmail.com'
AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL).hexdigest()
TWITTER_USERNAME = u''
GITHUB_USERNAME = u'krohx'
GITHUB_BADGE = True

# custom config variable for IRC
IRC_NICK = u''


# During development, we want urls to be relative
RELATIVE_URLS = True

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = 'Uncategorized'
DISPLAY_CATEGORIES_ON_MENU = True

TIMEZONE = 'Africa/Lagos'

PATH = 'content/'
#ARTICLE_DIR = PATH


SITEURL = 'http://krohx.github.io/blog'
# FEED_DOMAIN = SITEURL
# FEED_ATOM = 'feeds/main.atom.xml'
# FEED_RSS = 'feeds/main.rss.xml'
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
# TAG_FEED_ATOM = 'feeds/%s.atom.xml'
# TAG_FEED_RSS = 'feeds/%s.rss.xml'

# Feed generation is usually not desired when developing
# FEED_ATOM = None #'feeds/main.atom.xml'
# FEED_RSS = None #'feeds/main.rss.xml'
# FEED_ALL_ATOM = None
# FEED_ALL_RSS = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
# CATEGORY_FEED_ATOM = None
# CATEGORY_FEED_RSS = None
# TAG_FEED_ATOM = None
# TAG_FEED_RSS = None
# TRANSLATION_FEED_ATOM = None
# TRANSLATION_FEED_RSS = None



# metadata information: date and slug data from filename
FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'



SOCIAL_WIDGET_NAME = "Find  us on"
LINKS_WIDGET_NAME = "Bookmarks"

GRAB_ICONS = True

# Blogroll
#LINKS = (('Blog', '#0'),)

# Social widget
SOCIAL = (
	('github',
		'http://github.com/krohx'),
	('linkedin',
		'http://ng.linkedin.com/in/krohx'),
	('bitbucket',
		'http://bitbucket.org/krohx'),
	('Facebook', 'http://facebook.com/krohx')
	)
          
          #('Facebook', 'http://facebook.com/takwas')
          #('Twitter', 'http://twitter.com/acetakwas'),
          #('Google+', 'http://plus.google.com/+TosinAnimashaun/about?hl=en_GB')
          #('Youtube', 'youtube.com/acetakwas'),)




DEFAULT_PAGINATION = 10







# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for current theme
#THEME = '/home/acetakwas/dev/blog/pelican_themes/aboutwilson'
THEME = '/home/acetakwas/dev/blog/pelican_themes/gum'
#THEME = '/home/acetakwas/dev/blog/pelican_themes/tuxlite_zf'
#THEME = '/home/acetakwas/dev/blog/pelican_themes/new-bootstrap2'
#THEME = '/home/acetakwas/dev/blog/pelican_themes/tuxlite_tbs'
#THEME = '/home/acetakwas/dev/blog/pelican_themes/pelican-bootstrap3'
#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']


# Load thumbnail locally for development
SITE_THUMBNAIL = '/theme/img/avatar_krohx.png'
SITE_THUMBNAIL_TEXT = \
	'''
		A pen in hand,
		speaks volumes
	'''


MENUITEMS = (
	('Home', '/'),
	('About', '#about'),
)

SITESUBTITLE = SITE_TAGLINE

DISCLAIMER = False


# # Support for Disqus comments
# DISQUS_SITENAME = 'acetakwas-log'
