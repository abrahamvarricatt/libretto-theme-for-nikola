# -*- coding: utf-8 -*-

# Basic blog details
BLOG_AUTHOR = "BLOG_AUTHOR"
BLOG_TITLE = "BLOG_TITLE"
BLOG_DESCRIPTION = "BLOG_DESCRIPTION"
SITE_URL = "http://localhost:8000/"
BLOG_EMAIL = "no@email.here"
TIMEZONE = "America/Toronto"

# Blog configuration
THEME = "libretto"
DEFAULT_LANG = "en"
INDEX_DISPLAY_POST_COUNT = 4
INDEX_TEASERS = True
INDEX_PATH = "posts"
IMAGE_FOLDERS = {
    'images': 'images'
}
POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.rst", "", "story.tmpl"),
)
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/posts/index.html", "Blog"),
        ("/archive.html", "Archives"),
        ("/categories/index.html", "Tags"),
        ("/rss.xml", "RSS feed"),
    ),
}
# Configs to remove warnings
WRITE_TAG_CLOUD = True
USE_BUNDLES = False

# Third party integrations
COMMENT_SYSTEM = ""

