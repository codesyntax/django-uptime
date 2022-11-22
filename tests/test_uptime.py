from django.test import TestCase
from django.urls import reverse


class MainUrlsTestCase(TestCase):
    def setUp(self):
        pass

    def test_ok(self):
        response = self.client.get(reverse("uptime_index"))
        self.assertEqual(response.status_code, 200)
