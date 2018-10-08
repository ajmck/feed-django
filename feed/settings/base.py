import os
import dj_database_url
from django.utils import timezone
import django.contrib.gis

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "SECRETKEYFALLBACK")

ROOT_URLCONF = 'feed.urls'
WSGI_APPLICATION = 'feed.wsgi.application'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.humanize',
    'core.apps.CoreConfig',
    'rest_framework',
    'rest_framework_gis',
    'secretballot',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'secretballot.middleware.SecretBallotIpUseragentMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Set current timezone to NZ time
# Note this is different from Django's default timezone
# https://docs.djangoproject.com/en/2.1/topics/i18n/timezones/#default-current-time-zone
timezone.activate("NZ")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"


def tinybool(b):
    """
    Fun facts about OS.getenv:

    If a variable is defined in a .env file but contains no value, it will treat the value as "" instead of None
    Consequently, it won't fall back to the second argument of os.getenv()
    """
    if b is None:
        return False
    if isinstance(b, bool):
        # possible point of failure
        return b
    if str(b).lower() == 'true':
        return True
    if str(b).lower() == 'false' or str(b) == "":
        return False
    else:
        raise RuntimeError("Invalid boolean value: " + b)


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}


# Custom parameters
POST_BODY_LENGTH = 300
AZURE_CONTENT_MODERATOR_KEY = os.getenv("AZURE_CONTENT_MODERATOR_KEY")
GOOGLE_ANALYTICS_KEY = os.getenv("GOOGLE_ANALYTICS_KEY")
ENABLE_LOCATION = tinybool(os.getenv("ENABLE_LOCATION", True))
HERE_APP_ID = os.getenv("HERE_APP_ID")
HERE_APP_CODE = os.getenv("HERE_APP_CODE")
