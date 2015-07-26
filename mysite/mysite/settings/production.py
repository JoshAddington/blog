from .base import *
SECRET_KEY = os.environ['BLOG_SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOST'],
        'PORT': os.environ['RDS_PORT'],
        'CONN_MAX_AGE': 600,
    }
}
