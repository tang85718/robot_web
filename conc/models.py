# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Message(models.Model):
    # django 默认添加id primary key
    msg_id = models.IntegerField()
    type = models.IntegerField()


class SimpleMessage(models.Model):
    msg = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.CharField(max_length=2048)
    star = models.IntegerField()
    cls = models.IntegerField()
