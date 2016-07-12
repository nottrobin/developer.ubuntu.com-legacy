# -*- coding: utf-8 -*-
"""
Django settings for developer_portal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# System modules
import os

# Third party modules
import dj_database_url
from django.utils.translation import ugettext_lazy as _

ADMIN_GROUP = 'ubuntudeveloperportal'
EDITOR_GROUP = 'ubuntudeveloperportal-editors'
ALLOWED_HOSTS = ['127.0.0.1']
SITE_ID = 1

# SECRET_KEY environment variable must be set
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# Debug mode can be set with DJANGO_DEBUG=true, otherwise defaults to False
DEBUG = os.environ.get('DJANGO_DEBUG', '').lower() == 'true'

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_openid_auth',  # Allow login from Ubuntu SSO
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'reversion',  # content versioning
    'django_pygments',
    'django_comments',
    'tagging',
    'template_debug',
    'ckeditor',
    'djangocms_text_ckeditor',
    'cms',  # django CMS itself
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_snippet',
    'treebeard',
    'cmsplugin_zinnia',
    'zinnia',
    'zinnia_ckeditor',
    'developer_portal',
    'webapp_creator',
    'store_data',
    'api_docs',
    'md_importer',
]

# Locations for media files
STATIC_URL = '/static/'
STATIC_ROOT = "static"
MEDIA_ROOT = "media"
MEDIA_URL = '/media/'
ASSET_SERVER_URL = 'https://assets.ubuntu.com/v1/'

# SwiftStorage configs
if 'OS_TENANT_NAME' in os.environ:
    # Enable swiftstorage
    OS_TENANT_NAME = os.environ['OS_TENANT_NAME']
    OS_USERNAME = os.environ['OS_USERNAME']
    OS_PASSWORD = os.environ['OS_PASSWORD']
    OS_REGION_NAME = os.environ['OS_REGION_NAME']
    OS_AUTH_URL = os.environ.get('OS_AUTH_URL', '')

    INSTALLED_APPS += ['swiftstorage']
    DEFAULT_FILE_STORAGE = "swiftstorage.storage.SwiftStorage"
    SWIFT_CONTAINER_NAME = "developer.ubuntu.com-cms-media"

    print(
        "Using Swift container "
        "{OS_TENANT_NAME}@{OS_REGION_NAME}:{SWIFT_CONTAINER_NAME} "
        "for CMS media."
    ).format(**locals())
else:
    print(
        "No swift credentials found. "
        "Using local `{MEDIA_ROOT}` directory for CMS media."
    ).format(**locals())

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'developer_portal.middleware.CacheFriendlySessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'django.contrib.messages.context_processors.messages',
                'django_asset_server_url.asset_server_url',
            ]
        }
    }
]

ROOT_URLCONF = 'developer_portal.urls'
WSGI_APPLICATION = 'developer_portal.wsgi.application'

# Update database settings from DATABASE_URL environment variable
DATABASES = {
    'default': dj_database_url.config(
        default="postgres://postgres:dev@db:5432/postgres"
    )
}

# Internationalization (https://docs.djangoproject.com/en/1.6/topics/i18n/)
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Django CMS specific settings
CMS_PERMISSION = True
CMS_CACHE_DURATIONS = {
    'menus': 0,
    'content': 60,
    'permissions': 3600,
}
CMS_TEMPLATES = (
    ('default.html', 'Default'),
    ('landing_page.html', 'Landing Page'),
    ('no_subnav.html', 'Without Subnav'),
    ('with_hero.html', 'With Hero'),
    ('snappy_hero_tour.html', 'Snappy Hero Tour'),
)
LOCALE_PATHS = ['locale']
LANGUAGES = [
    ('en', _('English')),
    ('zh-cn', _('Simplified Chinese')),
]
CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': _('English'),
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback': False,
        },
        {
            'code': 'zh-cn',
            'name': _('Simplified Chinese'),
            'fallbacks': ['en'],
            'hide_untranslated': True,
            'redirect_on_fallback': False,
            'public': True,
        },
        {
            'code': 'es',
            'name': _('Spanish'),
            'fallbacks': ['en'],
            'hide_untranslated': False,
            'redirect_on_fallback': False,
            'public': True,
        },
    ],
    'default': {
        'fallbacks': ['en'],
        'redirect_on_fallback': False,
        'public': False,
        'hide_untranslated': False,
    }
}
AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# OPENID Related settings
OPENID_STRICT_USERNAMES = False
OPENID_FOLLOW_RENAMES = True
OPENID_SREG_REQUIRED_FIELDS = ['email']
OPENID_CREATE_USERS = True
OPENID_REUSE_USERS = False
OPENID_UPDATE_DETAILS_FROM_SREG = True
OPENID_SSO_SERVER_URL = 'https://login.ubuntu.com/'
OPENID_LAUNCHPAD_TEAMS_MAPPING_AUTO = True

# Tell django.contrib.auth to use the OpenID signin URLs.
LOGIN_URL = '/openid/login'
LOGIN_REDIRECT_URL = '/'

# Django 1.6 uses a JSON serializer by default, which breaks
# django_openid_auth, so force it to use the old default
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

CMS_PLACEHOLDER_CONF = {
    'page_content': {
        'name': _("Page content"),
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    # Translators: this is the default text that will be shown
                    # to editors when editing a page. You can use some HTML,
                    # but don't go wild :)
                    'body': _('<p>Add content here...</p>'),
                },
            },
        ],
    },
}

CKEDITOR_UPLOAD_PATH = "media/"
CKEDITOR_JQUERY_URL = (
    '//ajax.googleapis.com/'
    'ajax/libs/jquery/2.1.1/jquery.min.js'
)
CKEDITOR_IMAGE_BACKEND = 'dummy'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
    'zinnia-content': {
        'toolbar_Zinnia': [
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Undo', 'Redo'],
            ['Scayt'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Source'],
            ['Maximize'],
            '/',
            ['Bold', 'Italic', 'Underline', 'Strike',
             'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-',
             'Outdent', 'Indent', '-', 'Blockquote'],
            ['Styles', 'Format'],
        ],
        'toolbar': 'Zinnia',
    },
}

# Allow iframes in ckeditor
TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder')

CMSPLUGIN_ZINNIA_APP_URLS = ['developer_portal.blog.urls']

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

MIGRATION_MODULES = {
    'cms': 'cms.migrations',
    'cmsplugin_zinnia': 'cmsplugin_zinnia.migrations',
    'djangocms_link': 'djangocms_link.migrations',
    'djangocms_picture': 'djangocms_picture.migrations',
    'djangocms_snippet': 'djangocms_snippet.migrations',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations',
    'djangocms_video': 'djangocms_video.migrations',
    'django_comments': 'django_comments.migrations',
    'menus': 'menus.migrations',
    'rest_framework.authtoken': 'rest_framework.authtoken.migrations',
    'reversion': 'reversion.migrations',
    'tagging': 'tagging.migrations',
    'taggit': 'taggit.migrations',
    'zinnia': 'zinnia.migrations',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'normal': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './error.log',
            'formatter': 'normal',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
