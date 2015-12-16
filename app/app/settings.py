"""
Django settings for www project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kh-v7!hyo@=*hkqg_r42vo(&3jomj($yu-w4dx3ja%*y(g337x'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eleme',
)
#AUTHENTICATION_BACKENDS = ('apps.apployment_site.auth.CustomAuth',
 #  'tokenapi.backends.TokenBackend',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
 #   'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'
#WSGI_APPLICATION = 'eleme.views.index'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
host = os.getenv("DB_HOST", "localhost")
port = int(os.getenv("DB_PORT", "3306"))
name = os.getenv("DB_NAME", "eleme")
USER = os.getenv("DB_USER", "root")
PASSWORD = os.getenv("DB_PASS", "toor")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': name,                       
        'USER': USER,                       
        'PASSWORD': PASSWORD    ,                   
        'HOST': host,                           
        'PORT': port,                           
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TOKEN_TIMEOUT_DAYS = 7
TOKEN_CHECK_ACTIVE_USER = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
