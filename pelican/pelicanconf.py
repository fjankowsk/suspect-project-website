AUTHOR = "Dr Fabian Jankowski"
SITENAME = "The SUSPECT Project"
SITEURL = "https://suspectproject.com"

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# use better name for blog
DEFAULT_CATEGORY = "news"

PLUGIN_PATHS = ["./plugins"]
PLUGINS = []

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "noclasses": True,
            "pygments_style": "default",
            "use_pygments": True,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.toc": {},
    }
}

# use bootstrap3
THEME = "themes/pelican-bootstrap3"

# use custom CSS
CUSTOM_CSS = "static/custom.css"

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
    ("Fabian Jankowski", "https://fabian.jankowskis.org/"),
    ("Nançay Radio Observatory", "https://www.obs-nancay.fr/"),
    ("PSRCHIVE", "http://psrchive.sourceforge.net/"),
    ("DSPSR", "http://dspsr.sourceforge.net/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/fjankowsk"),
)

DEFAULT_PAGINATION = 20

STATIC_PATHS = ["extra"]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

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
    (2, "{base_name}/{number}/", "{base_name}/{number}/index.html"),
)

FAVICON = "favicon.ico"
