from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot_web.settings')

app = Celery('robot_web')
# app = Celery('robot_web',
#              broker='amqp://',
#              backend='amqp://',
#              include=['robot_web.tasks'])

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler',
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    CELERY_ACCEPT_CONTENT=['pickle', 'json', 'msgpack', 'yaml'],
    #: Only add pickle to this list if your broker is secured
    #: from unwanted access (see userguide/security.html)
    # CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
)


# Celery settings
# CELERY_TIMEZONE='Asia/Shanghai'
# BROKER_URL = 'amqp://guest:guest@localhost//'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend',
