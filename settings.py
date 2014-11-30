AUTHOR = "Justin Li"
SITENAME = "Justin Li"
SITEURL = "http://justinnhli.com"

MENUITEMS = (
    ("Tweets", "https://twitter.com/justinnhli/"),
    ("Writings", "http://justinnhli.com/writings.html"),
    ("Code", "https://github.com/justinnhli?tab=repositories"),
)

STATIC_PATHS = (
    "files/",
)

IGNORE_FILES = (
    ".*.un~", ".*.swp"
)

ARCHIVES_SAVE_AS = 'writings.html'

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}.html"

RELATIVE_URLS = True

DATE_FORMATS = {"en":"%Y-%m-%d",}
TIMEZONE = "America/Detroit"

THEME = "themes/justinnhli"

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ("archives",)

AUTHORS_SAVE_AS = False
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = False
TAG_SAVE_AS = False
