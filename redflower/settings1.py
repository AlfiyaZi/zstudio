
"""
Django settings for zakharova  project.

"""


import os
import sys

#from oscar import OSCAR_MAIN_TEMPLATE_DIR
#from django.utils.translation import ugettext_lazy as _
#from django.core.urlresolvers import reverse_lazy



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
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
#print "DB:", DATABASE_PATH
#print "OSCAR_MAIN_TEMPLATE_DIR:", OSCAR_MAIN_TEMPLATE_DIR

SECRET_KEY = 'nby*&16v#&h@*!0v%zxpqk5k$p1&r_*w3@yc5j=o(dz_1z^q%+'


EMAIL_SUBJECT_PREFIX = '[zakharova_studio ] '
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['xn--80abcfagd3c0abbba1av5dyb0cwa.xn--p1ai']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
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
]

from oscar import get_core_apps
INSTALLED_APPS = INSTALLED_APPS + get_core_apps()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)


SITE_ID = 1

ROBOKASSA_LOGIN ='flowerBigCity'
ROBOKASSA_PASSWORD1 ='lY7d2Shj28'
ROBOKASSA_PASSWORD2 ='4hc033wFtB'

ROBOKASSA_USE_POST = True
ROBOKASSA_STRICT_CHECK= False
ROBOKASSA_TEST_MODE = False
ROBOKASSA_EXTRA_PARAMS = []



ROOT_URLCONF = 'zstudio.urls'

WSGI_APPLICATION = 'zstudio.wsgi.application'


# Database


DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xnabcfag_zstudio',
        'USER': 'xnabcfag_zadmin,',
        'PASSWORD': 'kKGk0]zEmcv&',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}


LOGIN_REDIRECT_URL = '/catalogue/'
APPEND_SLASH = True








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
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

from oscar import OSCAR_MAIN_TEMPLATE_DIR
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
   # OSCAR_MAIN_TEMPLATE_DIR,
)


# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'app_namespace.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # needed by django-treebeard for admin (and potentially other libs)
    'django.template.loaders.eggs.Loader',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'checkout_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'checkout.log',
            'formatter': 'verbose'
        },
        'gateway_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'gateway.log',
            'formatter': 'simple'
        },
        'error_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'errors.log',
            'formatter': 'verbose'
        },
        'sorl_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'sorl.log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        # Django loggers
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
        # Oscar core loggers
        'oscar.checkout': {
            'handlers': ['console', 'checkout_file'],
            'propagate': False,
            'level': 'INFO',
        },
        'oscar.catalogue.import': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        'oscar.alerts': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'INFO',
        },
        # Sandbox logging
        'gateway': {
            'handlers': ['gateway_file'],
            'propagate': True,
            'level': 'INFO',
        },
        # Third party
        'south': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'sorl.thumbnail': {
            'handlers': ['sorl_file'],
            'propagate': True,
            'level': 'INFO',
        },
        # Suppress output of this debug toolbar panel
        'template_timings_panel': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        }
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
INTERNAL_IPS = ['127.0.0.1', '::1','89.179.14.20',]



# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "public/media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/admin/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'public/static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)







# We still use this deprecated Django setting since Oscar needs a way of
# knowing where the profile class is (if one is used).
#AUTH_PROFILE_MODULE = 'user.Profile'


# Logging
# =======

LOG_ROOT = os.path.join(PROJECT_PATH, 'logs')
# Ensure log root exists
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)


from oscar.defaults import *

OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = True

OSCAR_SHOP_NAME = 'flowers'
OSCAR_SHOP_TAGLINE = ''


#USE_LESS = True
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

THUMBNAIL_KEY_PREFIX = 'flowers'


# Currency
OSCAR_DEFAULT_CURRENCY = ''
OSCAR_CURRENCY_LOCALE = 'RU'

# Registration
OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_FROM_EMAIL = 'florgreen@bk.ru'


# Address settings
OSCAR_REQUIRED_ADDRESS_FIELDS = ( 'last_name', 'line1'
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


