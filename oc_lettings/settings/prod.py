from .base import *
import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

USE_TZ = False

django_heroku.settings(locals())


sentry_sdk.init(
    dsn="https://5366f49b7c2543c08e58281024ff472e@o1417074.ingest.sentry.io/4504003434250240",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
