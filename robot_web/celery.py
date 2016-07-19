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
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.requset))

# if __name__ == '__main__':
#     app.start()
