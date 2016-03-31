"""
Django settings for django_cloudsql project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vabda(a6j2uk92w=3z)y5ghfo6*7vb@*f&dw$@3az6*67+f^@r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# See https://developers.google.com/appengine/docs/python/cloud-sql/django#development-settings

APP_ENGINE = os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cloudsql',
)

if not APP_ENGINE:
  INSTALLED_APPS = INSTALLED_APPS + ('django_nose',)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
  '--with-xunit', '--xunit-file=shippable/testresults/test.xml',
  '--with-coverage', '--cover-xml', '--cover-xml-file=shippable/codecoverage/coverage.xml',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_cloudsql.urls'

WSGI_APPLICATION = 'django_cloudsql.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# See https://developers.google.com/appengine/docs/python/cloud-sql/django#development-settings

if APP_ENGINE:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'HOST': '/cloudsql/testgkeproject-1181:steph-sql-instance-1',
          'NAME': 'django_test',
          'USER': 'root',
      }
  }
elif os.getenv('SETTINGS_MODE') == 'prod':
    # Running in development, but want to access the Google Cloud SQL instance
    # in production.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'INSTANCE': '2001:4860:4864:1:f46e:ede4:99d6:8c2e ',
            'NAME': 'django_test',
            'USER': 'root',
        }
    }
else:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'test',
          'USER': 'shippable',
      }
  }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
