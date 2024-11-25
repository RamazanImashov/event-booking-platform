from decouple import config


SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
        "REDIRECT_URL": config("LOGIN_REDIRECT_URL")
    }
}


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = "optional"  # 'none', 'optional', 'mandatory'
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGIN_REDIRECT_URL = config("LOGIN_REDIRECT_URL")  # Измените по вашему усмотрению
SOCIALACCOUNT_LOGIN_ON_GET = True

