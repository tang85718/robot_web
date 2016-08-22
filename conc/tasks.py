# coding:utf-8
from __future__ import absolute_import
from robot_web.celery import app
from celery import shared_task
from channels import Group
from scrapy.cmdline import execute
import time

# @app.task
@shared_task
def helloCelery():
    print('Hello, Celery')
    return 'Hello, Celery'


@app.task
def add(x, y):
    return x + y


@app.task
def send_test():
    FORMAT = '%Y-%m-%d %X'
    now = time.strftime(FORMAT, time.localtime())
    Group("conc").send({
        "text": "today is " + now
    })


@app.task
def crawl_jin10():
    execute(['scrapy', 'crawl', 'jin10'])
