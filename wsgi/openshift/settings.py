"""
Django settings for openshift project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates/'),)
LOGIN_REDIRECT_URL = '/'


# Running on OpenShift ?
ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if ON_OPENSHIFT:
    try:
        SECRET_KEY = os.environ['DJANGO_SETTINGS_SECRET_KEY']
    except KeyError:
        print("Please create env variable DJANGO_SETTINGS_SECRET_KEY (cf README)")
else:
    SECRET_KEY = os.environ['BLOG_SECRET_KEY'] # dev key

# SECURITY WARNING: don't run with debug turned on in production!
if ON_OPENSHIFT and os.environ['OPENSHIFT_GEAR_DNS'] == 'mysite-addington.rhcloud.com':
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = True

# Enable debug for only selected hosts
if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['*']

# List of admins (+ 500 error report by mail)
ADMINS = (
    ('Josh', 'dragonorta@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS += (
    'blog',
    'projects',
    'social.apps.django_app.default',
    'citibike'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'openshift.urls'

WSGI_APPLICATION = 'openshift.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if ON_OPENSHIFT:  # production settings
    DATABASES = {
        'default': {  # you can change the backend to any django supported
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME':     os.environ['OPENSHIFT_APP_NAME'],
            'USER':     os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
            'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
            'HOST':     os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
            'PORT':     os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
        }
    }
else:  # dev settings
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'citidb',
            'USER': os.environ['BLOG_DB_USER'],
            'PASSWORD': os.environ['BLOG_DB_PASSWORD'],
            'HOST': '',
            'PORT': '',
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Grappelli template settings
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

if 'OPENSHIFT_REPO_DIR' in os.environ:
    STATIC_ROOT = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR'), 'wsgi', 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# Python Social Auth Settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GooglePlusAuth',
)

MIDDLEWARE_CLASSES += (
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

SOCIAL_AUTH_FACEBOOK_KEY = os.environ['SOCIAL_FACEBOOK_KEY']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['SOCIAL_FACEBOOK_SECRET']

SOCIAL_AUTH_GOOGLE_PLUS_KEY = os.environ['SOCIAL_GOOGLE_CLIENT_ID']
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = os.environ['SOCIAL_GOOGLE_CLIENT_SECRET']

SOCIAL_AUTH_TWITTER_KEY = os.environ['SOCIAL_TWITTER_CONSUMER_KEY']
SOCIAL_AUTH_TWITTER_SECRET = os.environ['SOCIAL_TWITTER_CONSUMER_SECRET']

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_URL_NAMESPACE = 'social'

TEMPLATE_CONTEXT_PROCESSORS += (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)
