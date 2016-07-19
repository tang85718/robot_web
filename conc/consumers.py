# coding:utf-8
from channels import Group


def ws_connect(message):
    Group('conc').add(message.reply_channel)


def ws_receive(message):
    pass


def ws_disconnect(message):
    Group('conc').discard(message.reply_channel)
