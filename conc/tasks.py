from __future__ import absolute_import
from robot_web.celery import app
from celery import shared_task

# @app.task
@shared_task
def helloCelery():
    print('Hello, Celery')
    return 'Hello, Celery'