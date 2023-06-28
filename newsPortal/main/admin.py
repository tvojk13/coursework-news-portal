from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('header',)}
    list_display = ('header', 'categoryKey', 'date', 'published')
admin.site.register(News, NewsAdmin)

# Register your models here.
