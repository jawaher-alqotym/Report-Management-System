# report_management/settings/dev.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = [
      '127.0.0.1',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
