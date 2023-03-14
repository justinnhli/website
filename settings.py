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

# this controls which collections pages are generated
# possible values: index, authors, categories, tags, archives
DIRECT_TEMPLATES = ('archives',)

ARCHIVES_SAVE_AS = 'writings.html'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

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

AUTHORS_SAVE_AS = False
TAGS_SAVE_AS = False

AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
