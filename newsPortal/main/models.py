from django.db import models

class News(models.Model):
    date = models.DateTimeField('Дата')
    header = models.CharField('Заголовок', max_length=255)
    article = models.TextField('Статья')
    published = models.BooleanField('Опубликовано', default=False)

# Create your models here.
