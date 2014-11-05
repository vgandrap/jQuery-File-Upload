"""
Django settings for imageUpload project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8@p=h%o8(r_-p$a-^itfl^y+hsygr-^izz$3vj*)w6((^wb_sg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar.apps.DebugToolbarConfig',
    "django_extensions",
    'fileupload',
    'imagekit',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'imageUpload.urls'

WSGI_APPLICATION = 'imageUpload.wsgi.application'

#Amazon S3 Storage
#DEFAULT_FILE_STORAGE = 'mysite.s3utils.MediaRootS3BotoStorage'
#AWS_S3_SECURE_URLS = False       # use http instead of https
#AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
#AWS_UPLOAD_CLIENT_KEY_ID = '********************'     # enter your access key id
#AWS_UOPLOAD_CLIENT_SECRET_KEY = '****************************************' # enter your secret access key
#AWS_UPLOAD_BUCKET_NAME = 'minidjangoproject'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
#MEDIA_subROOT = os.path.abspath(os.path.join(BASE_DIR, "vijay"))
#MEDIA_ROOT = os.path.abspath(os.path.join(MEDIA_subROOT, "media"))
MEDIA_ROOT = os.path.abspath(os.path.dirname(__file__)) + '/media/'
