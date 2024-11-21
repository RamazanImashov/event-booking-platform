from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _
from ..setting.hepler import *
import cloudinary_storage
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = BASE_APPS + LIBS_APPS + APPS

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

SITE_ID = 1

MIDDLEWARE = BM

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = APVS

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

Redis_Host = config("REDISHOST")

CELERY_BROKER_URL = f'redis://{Redis_Host}:6379/0'
CELERY_RESULT_BACKEND = f'redis://{Redis_Host}:6379/0'

JAZZMIN_SETTINGS = JBS
JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

REST_FRAMEWORK = RF_BS

SIMPLE_JWT = JWT_BS

SPECTACULAR_SETTINGS = SP_BS

LOGGING = LOG_BS

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": F"redis://{Redis_Host}:6379/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
