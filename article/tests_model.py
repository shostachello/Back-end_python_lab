from django.test import TestCase

from .models import Article


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

    def test_get_absolute_url(self):
        article = Article.objects.get(id=5)
        self.assertEquals(article.get_absolute_url(), '/articles/2022/04/26/title-1')

    def test__str__(self):
        article = Article.objects.get(id=5)
        self.assertEquals(f'{article}', article.__str__())
