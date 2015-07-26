from .base import *

SECRET_KEY = 'dg+-h95=_*9+6s1@#9!*52+@ohzsixi@-7(ssyj9_5llrg*@f3k12g5'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'citidb',
        'USER': 'josh',
        'PASSWORD': 'devpassword',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
