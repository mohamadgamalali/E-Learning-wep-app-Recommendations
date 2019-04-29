from django.test import SimpleTestCase
from django.urls import reverse, resolve
from companyRecommendation.views import index, detail, CompanyList


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_detail_url_is_resolved(self):
        url = reverse('detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, detail)
