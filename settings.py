AUTHOR = "Justin Li"
SITENAME = "Justin Li"
SITEURL = "http://justinnhli.com"

MENUITEMS = (
    ("Essays", SITEURL + "/archives.html"),
    ("Code", "https://github.com/justinnhli?tab=repositories"),
    ("Twitter", "https://twitter.com/justinnhli/"),
)

STATIC_PATHS = (
    'files/',
)

RELATIVE_URLS = True

DATE_FORMATS = {'en':"%Y-%m-%d, %a",}
TIMEZONE = "America/Detroit"

THEME = "themes/justinnhli"

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
