import os
from celery import Celery
from celery.signals import setup_logging
from django.conf import settings
from logging.config import dictConfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@setup_logging.connect
def config_loggers(*args, **kwargs):
    if hasattr(settings, 'LOGGING'):
        dictConfig(settings.LOGGING)
