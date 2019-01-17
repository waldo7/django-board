from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomeView
# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolve_home_view(self):
        view = resolve('/')
        self.assertEquals(view.view_name, 'home')
        # self.assertEquals(view.func.view_class, HomeView)
