import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .settings import *

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
