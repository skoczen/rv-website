import logging
import json

from utils.helpers import reverse
from django.core import mail
from django.conf import settings
from django.test.utils import override_settings
from django.template.loader import render_to_string, get_template

from people.models import Person
from archives.models import HistoricalEvent
from inkmail.models import Subscription, OutgoingMessage
from inkmail.tasks import process_outgoing_message_queue
from utils.factory import Factory
from utils.test_helpers import MockRequestsTestCase
from utils.encryption import normalize_lower_and_encrypt, normalize_and_encrypt, encrypt, decrypt
import mock
import unittest


class TestHomePage(MockRequestsTestCase):

    def test_home_page_renders(self):
        url = reverse('website:home',)
        response = self.get(url)
        self.assertEquals(response.status_code, 200)
        resp_content = str(response.content)

        self.assertIn("Ronan", resp_content)
