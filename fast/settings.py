#set encoding=utf-8

import os
import sys

from oscar import OSCAR_MAIN_TEMPLATE_DIR
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')


# Printing paths for sanity
print "Settings directory:", SETTINGS_DIR
print "Project root:", PROJECT_PATH
print "Templates:", TEMPLATE_PATH
print "Static:", STATIC_PATH




DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xnabcfag_fast',
        'USER': 'xnabcfag_f',
        'PASSWORD': 'ffJpLV)1KC]L',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


ALLOWED_HOSTS = []


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


ROBOKASSA_LOGIN ='flowerBigCity'
ROBOKASSA_PASSWORD1 ='lY7d2Shj28'
ROBOKASSA_PASSWORD2 ='4hc033wFtB'
ROBOKASSA_USE_POST = True
ROBOKASSA_STRICT_CHECK= False
ROBOKASSA_TEST_MODE = False
ROBOKASSA_EXTRA_PARAMS = []




MEDIA_ROOT = os.path.join(PROJECT_PATH, "public/media")

MEDIA_URL = '/media/'


STATIC_URL = 'public/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'public/static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    
)

SECRET_KEY = 'e)umjngz*)@8mhd_6!6kce(y2lm)d089g)^7l1e6#z$&cc=%6w'




from oscar import OSCAR_MAIN_TEMPLATE_DIR
TEMPLATE_DIRS = (
     TEMPLATE_PATH,
     #OSCAR_MAIN_TEMPLATE_DIR,
)




TEMPLATE_LOADERS = (
    #'app_namespace.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # needed by django-treebeard for admin (and potentially other libs)
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)



AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',

    'django.contrib.auth.backends.ModelBackend',

)


MIDDLEWARE_CLASSES = (

    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.middleware.transaction.TransactionMiddleware',  
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',


)





ROOT_URLCONF = 'fast.urls'


WSGI_APPLICATION = 'fast.wsgi.application'



from oscar import get_core_apps

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'debug_toolbar',
    'treebeard',
    'template_timings_panel',
    'south',
    'compressor',
    'pagination',
    'bootstrap_pagination',
    'widget_tweaks',
    'florists',
    'about',
    'pages',
    'contact',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'mptt',  
    'menus',  
    'sekizai',    
    'adminsortable',
    'sorl.thumbnail',
    'portfolio',
    'pay',
    'tagging',
    'apps.invoice',
    'robokassa',
] + get_core_apps([ 'apps.checkout',  'apps.shipping'])

  


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'



# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}


LOGIN_REDIRECT_URL = '/catalogue/'
APPEND_SLASH = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



# =============
# Debug Toolbar
# =============

# Implicit setup can often lead to problems with circular imports, so we
# explicitly wire up the toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


INTERNAL_IPS = ['127.0.0.1', '::1','89.179.4.72',]




# Logging
# =======

LOG_ROOT = os.path.join(PROJECT_PATH, 'logs')
# Ensure log root exists
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)




#############

#set encoding=utf-8

# Meta
# ====


from oscar.defaults import *


OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country')
OSCAR_REQUIRED_ADDRESS_FIELDS += ('phone_number',)
OSCAR_SHOP_NAME = u'Студия флористики Елены Захаровой'
OSCAR_SHOP_TAGLINE = u'доставка букетов'
OSCAR_DEFAULT_CURRENCY = u'руб.'
OSCAR_CURRENCY_LOCALE = 'ru_RU'
OSCAR_CURRENCY_FORMAT = u'#,##0.00 ¤'

OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_ALLOW_ANON_REVIEWS = False
OSCAR_MODERATE_REVIEWS = True
# Registration
OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_FROM_EMAIL = 'florgreen@bk.ru'





###########




#USE_LESS = True
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)


# Sorl
# ====

THUMBNAIL_DEBUG = True
THUMBNAIL_KEY_PREFIX = 'florgreen'

# Use a custom KV store to handle integrity error
THUMBNAIL_KVSTORE = 'oscar.sorl_kvstore.ConcurrentKVStore'

# Django 1.6 has switched to JSON serializing for security reasons, but it does not
# serialize Models. We should resolve this by extending the
# django/core/serializers/json.Serializer to have the `dumps` function. Also
# in tests/config.py

# Search facets


DISPLAY_VERSION = False

USE_TZ = True

