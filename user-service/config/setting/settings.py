from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY')

AUTH_USER_MODEL = 'users.User'

ALLOWED_HOSTS = ("*",)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME'),
        'USER': config('DB_USER'),
        "PASSWORD": config('DB_PASS'),
        'HOST': config('DB_HOST'),
        'PORT': 5432,
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

STATIC_URL = "/back-static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back-static")

MEDIA_URL = '/back-media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "back-media")

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8003"]

# CORS_ALLOWED_ORIGINS = []

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    "HEAD",
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

