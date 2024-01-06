"""Django AIO"""
import os

import environ
from django.contrib.messages import constants as message_constants
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from version import VERSION

from datetime import timedelta

from typing import Any, Dict

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('main')
CONF_DIR = ROOT_DIR.path('config')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env('.env')

SECRET_KEY = env("SECRET_KEY", default='8na#(#x@0i*3ah%&$-q)b&wqu5ct_a3))d8-sqk-ux*5lol*wl')

DEBUG = env.bool("DEBUG", False)

SITE_ID = int(env("SITE_ID", default='1'))

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_spectacular',
    'drf_spectacular_sidecar',

    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_tracking',
    'crequest',  # noqa
    'channels',
    'corsheaders',  # noqa

    'main.api',
    'main.core',
    'main.notify',
    'main.users',
    'main.web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crequest.middleware.CrequestMiddleware',  # noqa
    'corsheaders.middleware.CorsMiddleware',  # noqa
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path('templates')), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.core.context_processors.site',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

WSGI_APPLICATION = 'config.wsgi.application'

ROOT_URLCONF = 'config.urls'

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'main.users.backends.UserModelBackend',
)

LOGIN_URL = reverse_lazy("users:login_view")

ADMIN_URL = env('ADMIN_URL', default="admin/")

LOCALE_PATHS = (str(APPS_DIR('locale')), str(CONF_DIR('locale')),)

LANGUAGE_CODE = env('LANGUAGE_CODE', default="en")

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('Français')),
    ('de', _('Deütsche')),
    ('tr', _('Türkçe')),  # noqa
    ('ar', _('العربية')),  # noqa
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_TITLE = "DjangoAIO site admin"
SITE_HEADER = "DjangoAIO administration"
INDEX_TITLE = "Dashboard administration"

SITE_NAME = env("SITE_NAME", default="DjangoAIO")
BASE_URL = env("BASE_URL", default="http://localhost:8000")

MESSAGE_TAGS = {
    message_constants.DEBUG: 'info',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

STATIC_ROOT = str(ROOT_DIR('public/static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (str(APPS_DIR.path('static', )),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = str(ROOT_DIR('public/media'))

MEDIA_URL = '/media/'

REDIS_PORT = int(os.environ.get('REDIS_PORT', default=6379))
REDIS_DB = int(os.environ.get('REDIS_DB', default=0))
REDIS_HOST = os.environ.get('REDIS_HOST', default='redis')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', default=None)
REDIS_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

if REDIS_PASSWORD:
    REDIS_URI = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

DEFAULT_REDIS_EXPIRE = int(os.environ.get('DEFAULT_REDIS_EXPIRE', default=120))

ASGI_APPLICATION: str = "config.routing.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URI, ],
        },
    },
}

DEFAULT_USER_AVATAR = STATIC_URL + "assets/img/user.png"
DEFAULT_USER_FOLDER = "users"

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# API SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = r'^/api/.*$'
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'DjangoAIO API',
    'DESCRIPTION': 'DjangoAIO API documentation',
    'VERSION': VERSION,
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',  # noqa
}
SPECTACULAR_DEFAULTS: Dict[str, Any] = {
    'SERVE_AUTHENTICATION': 'rest_framework_simplejwt.authentication.JWTAuthentication',
    'SERVE_PERMISSIONS': 'rest_framework.permissions.IsAuthenticated',
    'SERVE_FILTER_BACKEND': 'rest_framework.filters.SearchFilter',
    'SERVE_FILTER_FIELD': 'search',
    'SERVE_FILTER_SEARCH_PARAM': 'q',
    'SERVE_FILTER_ORDERING_PARAM': 'ordering',
}
