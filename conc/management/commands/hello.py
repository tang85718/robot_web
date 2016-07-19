# coding: utf-8
from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError
from channels import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Hello Commands')

        # def handle(self, *args, **options):
        #     index = 0
        #     while True:
        #         try:
        #             Group('conc').send('data %s' % ++index)
        #         except CommandError:
        #             raise CommandError('error')
