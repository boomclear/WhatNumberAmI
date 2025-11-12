from django.test import SimpleTestCase
from django.urls import reverse, resolve
from frontend.views import *


class TestsUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse(index)
        self.assertEquals(index, resolve(url).func)

    def test_userUpload_url_is_resolved(self):
        url = reverse(userUpload)
        self.assertEquals(userUpload, resolve(url).func)

    def test_userResultPage_url_is_resolved(self):
        url = reverse(userResultPage)
        self.assertEquals(userResultPage, resolve(url).func)
