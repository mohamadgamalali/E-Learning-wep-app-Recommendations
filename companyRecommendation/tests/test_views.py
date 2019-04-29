from django.test import TestCase, Client
from django.urls import reverse
from companyRecommendation.models import Company


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.detail_url = reverse('detail', args=['Details'])
        self.project1 = Company.objects.creat(
            name='Details',
            companyRecommendation=100000
        )

    def test_index(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companyRecommendation/index.html')

    def test_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companyRecommendation/detail.html')
