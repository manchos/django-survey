# -*- coding: utf-8 -*-

import logging
import os
from decouple import config, Csv

try:
    import colorama
except:
    from pip._vendor import colorama

colorama.init()

print(
    "\033[33m"
    "You're using a dev settings file. It includes django rosetta (in order "
    " for dev to update translations) that is only useful for dev. "
    "If you're a developper you need to 'pip3 install -e \".[dev]\"', "
    "If you want to use the app without doing your own settings you should"
    " remove django-rosetta from the installed apps in the settings."
    "\033[39m"
)

DEBUG = config('DEBUG', default=True, cast=bool)
ROOT = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = os.path.join(ROOT, "csv")
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s.%(funcName)s() l.%(lineno)s -\033[32m %(message)s \033[39m",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': config('DB_NAME'),
    }
}

USER_DID_NOT_ANSWER = "Left blank"

TEX_CONFIGURATION_FILE = os.path.join(ROOT, "doc", "example_conf.yaml")
SURVEY_DEFAULT_PIE_COLOR = "red!50"

SITE_ID = 1
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = "/media/"
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(ROOT, "media")
STATIC_ROOT = os.path.join(ROOT, "static")

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

DEBUG_ADMIN_NAME = "test_admin"
DEBUG_ADMIN_PASSWORD = "test_password"

STATICFILES_DIRS = [os.path.normpath(os.path.join(ROOT, "..", "survey", "static"))]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "js*79rk(+s+x9)8co+10$zghe2f)+33jd1l2m#f)vl+pvtj24e"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(ROOT, "survey", "templates"),
            os.path.join(ROOT, "dev", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                # Default
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "urls"
WSGI_APPLICATION = "wsgi.application"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "survey",
    "bootstrapform",
    "rosetta",
)

LOCALE_PATHS = (os.path.join(ROOT, "survey", "locale"),)
LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", "english"),
    ('ru', 'russian'),
    ("es", "spanish"),
    ("fr", "french"),
    ("ja", "Japanese"),
    ("zh", "Chinese"),
)

LOGIN_REDIRECT_URL = "/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        }
    },
}
