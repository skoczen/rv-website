import logging
import json

from django.core import mail
from django.conf import settings
from django.urls import reverse
from django.template.loader import render_to_string, get_template
from django.test import TestCase
import mock
import unittest


class TestHomePage(TestCase):

    def test_home_page_renders(self):
        url = reverse('website:home',)
        response = self.get(url)
        self.assertEquals(response.status_code, 200)
        resp_content = str(response.content)

        self.assertIn("Ronan", resp_content)
