from .settings_base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'survey.darken.gen.tr',
    'survey-api.darken.gen.tr'
]

CSRF_TRUSTED_ORIGINS = [
    'https://survey.darken.gen.tr',
    'https://survey-api.darken.gen.tr'
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = [
    "https://survey.darken.gen.tr",
    'https://survey-api.darken.gen.tr'
]


SIMPLE_JWT = {
    'USER_ID_FIELD': 'email',
    'USER_ID_CLAIM': 'email',
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': env('PGPORT')
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

