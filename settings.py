AUTHOR = 'Justin Li'
SITENAME = 'Justin Li'
SITEURL = 'http://justinnhli.com'

MENUITEMS = (
    ('Tweets', 'https://twitter.com/justinnhli/'),
    ('Writings', '/writings.html'),
    ('Code', 'https://github.com/justinnhli?tab=repositories'),
)

STATIC_PATHS = (
    '.htaccess',
    'files/',
)

IGNORE_FILES = (
    '.*.un~',
    '.*.swp',
)

ARCHIVES_SAVE_AS = 'writings.html'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'

DATE_FORMATS = {'en':'%Y-%m-%d',}
TIMEZONE = 'America/Los_Angeles'

THEME = 'themes/justinnhli'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'guess_lang': False,
            'css_class': 'codehilite',
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ('archives',)

AUTHORS_SAVE_AS = False
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAGS_SAVE_AS = False
TAG_SAVE_AS = False
