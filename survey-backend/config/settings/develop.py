from datetime import timedelta

from .settings_base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tx4p1f)-ko10ywl_ow3+!qggrhbw4f&1!6*+!th+t-d=x*41vk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://localhost:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(seconds=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    'USER_ID_FIELD': 'email',
    'USER_ID_CLAIM': 'email',
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]
