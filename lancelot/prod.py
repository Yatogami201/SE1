from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "lancelot",
        "USER": "lancelot",
        "PASSWORD": "lancelot",
        "HOST": "localhost",
    }
}
