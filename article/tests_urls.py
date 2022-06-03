from django.test import TestCase
from django.urls import reverse

from article.models import Article


class ArticleTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            id=5,
            title='title 1',
            description='description1',
            pub_date='2022-04-26',
            slug='title-1'
        )

    def test_article_list(self):
        url = reverse('articles-list', )
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_article_details(self):
        url = reverse('news-detail', args=('2022', '04', '26', 'title-1'))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

