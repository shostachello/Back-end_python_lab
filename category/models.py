from django.db import models
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(u'Категорія', max_length=250, help_text=u'Максимум 250 символів')
    slug = models.SlugField(u'Слаг')

    class Meta:
        verbose_name = u'Категорія для новини'
        verbose_name_plural = u'Категорії для новин'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse('articles-category-list',
                          kwargs={'slug': self.slug})
        except:
            url = "/"
        return url
