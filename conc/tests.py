from django.test import TestCase
from django.core.management import call_command
from models import Message, SimpleMessage


# Create your tests here.

class DatabaseTests(TestCase):
    def test_insert_data(self):
        Message.objects.all().delete()

        for i in range(100):
            msg = Message.objects.create(msg_id=10001, type=1)
            msg.save()

        data_list = Message.objects.all()
        self.assertEqual(100, data_list.count(), msg="actual count=" + str(data_list.count()))

        # simple = SimpleMessage.objects.create(msg=msg, star=1)
        # simple.content = json.
