AUTHOR = "Justin Li"
SITENAME = "Justin Li"
SITEURL = "http://justinnhli.com"

MENUITEMS = (
    ("Essays", SITEURL + "/archives.html"),
    ("Code", "https://github.com/justinnhli?tab=repositories"),
    ("Twitter", "https://twitter.com/justinnhli/"),
)

STATIC_PATHS = (
    "files/",
)

IGNORE_FILES = (
    ".un~",
)

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"

RELATIVE_URLS = True

DATE_FORMATS = {"en":"%Y-%m-%d",}
TIMEZONE = "America/Detroit"

THEME = "themes/justinnhli"

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ("archives",)

AUTHORS_SAVE_AS = False
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = False
TAG_SAVE_AS = False
