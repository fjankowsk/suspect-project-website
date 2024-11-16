AUTHOR = 'Dr Fabian Jankowski'
SITENAME = 'The SUSPECT project'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# use better typography
TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# add date to output filenames and drafts
ARTICLE_URL = "{date:%Y-%m-%d}.{slug}/"
ARTICLE_SAVE_AS = "{date:%Y-%m-%d}.{slug}/index.html"
DRAFT_URL = "drafts/{date:%Y-%m-%d}.{slug}/"
DRAFT_SAVE_AS = "drafts/{date:%Y-%m-%d}.{slug}/index.html"

# use separate directories for pages and categories
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

# use nice urls for tags
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# we don't need the authors page
AUTHOR_SAVE_AS = ""

# archives
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"

# use nice urls here as well
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = "archives/index.html"
AUTHORS_SAVE_AS = ""
CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"
TAGS_URL = "tag/"
TAGS_SAVE_AS = "tag/index.html"

# use nice urls for pagination as well
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)
