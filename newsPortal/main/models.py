from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse


class News(models.Model):
    date = models.DateTimeField('Дата')
    header = models.CharField('Заголовок', max_length=255)
    article = models.TextField('Статья')
    published = models.BooleanField('Опубликовано', default=False)
    important = models.BooleanField('Важная новость', default=False)
    categoryKey = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Ссылка')
    picture = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Картинка')

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('news', kwargs={'slug': self.slug})


class Category(models.Model):
    categoryNameRU = models.CharField(max_length=50, db_index=True)
    categoryNameENG = models.CharField(max_length=50, db_index=True, null=True)

    def __str__(self):
        return self.categoryNameRU

    def get_absolute_url(self):
        return reverse('category', kwargs={'categoryNameRU': self.categoryNameENG})

# Create your models here.
