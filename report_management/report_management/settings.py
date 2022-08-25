# setting.py

import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from elasticsearch import RequestsHttpConnection

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^kg*85-z&h^#cex1@3_lj%ns9z!c(3zvbopu)*iwzg!^@6^n9q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Rest app
    'rest_framework',

    #django_storages app
    'storages',

    # project apps
    'users_management_app',
    'reports_management_app',
    'search_app',# Elasticsearch integration with the Django

    # Django Elasticsearch integration
    'django_elasticsearch_dsl',

    # Django REST framework Elasticsearch integration (this package)
    'django_elasticsearch_dsl_drf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'report_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'report_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ReportManagementdb',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('ReportManagementdb_password') ,
        'HOST': 'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS s3 bucket
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'django-report-management'

# to prevent files with similar name from over writing each other
AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_ADDRESSING_STYLE = 'virtual'
AWS_S3_SIGNATURE_VERSION = 's3v4'

# jwt token life span
SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60*24),
'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
'ROTATE_REFRESH_TOKENS': False,
'BLACKLIST_AFTER_ROTATION': False,
'UPDATE_LAST_LOGIN': False,
'ALGORITHM': 'HS256',
'SIGNING_KEY': SECRET_KEY,
'VERIFYING_KEY': None,
'AUDIENCE': None,
'ISSUER': None,
'JWK_URL': None,
'LEEWAY': 0,
'AUTH_HEADER_TYPES': ('Bearer',),
'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
'USER_ID_FIELD': 'id',
'USER_ID_CLAIM': 'user_id',
'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
'TOKEN_TYPE_CLAIM': 'token_type',
'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
'JTI_CLAIM': 'jti',
'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
'SLIDING_TOKEN_LIFETIME': timedelta(minutes=60*24),
'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'ORDERING_PARAM': 'ordering',
}

# Elasticsearch configuration
from elasticsearch import RequestsHttpConnection

# Elasticsearch configuration in settings.py
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200',
        'use_ssl': True,
        'http_auth': ('elastic', 'z9JeaMwCFP3ivwHHfvnv'),
        'verify_certs': False,
        'ca_certs': None, #'/path/to/cert.crt',
        'connection_class': RequestsHttpConnection
    }
}