import os

from django.conf import settings
from django.shortcuts import render, HttpResponse, get_object_or_404
from datetime import datetime
from .models import *
from django.utils.text import slugify

menu = [
    {'title': 'Мир', 'url_name': 'world'},
    {'title': 'Спорт', 'url_name': 'sport'},
    {'title': 'Культура', 'url_name': 'culture'},
    {'title': 'Экономика', 'url_name': 'economic'},
    {'title': 'Кино', 'url_name': 'cinema'},
    {'title': 'Эксклюзивы', 'url_name': 'exclusive-news'},
    {'title': 'Редакция', 'url_name': 'about'},
]


def index(request):
    content = News.objects.all().order_by('date')
    now = datetime.now()
    topToday = News.objects.filter(date__year=now.year, date__month=now.month, date__day=now.day)

    context = {
        'content': content,
        'topToday': topToday,
        'menu': menu,
    }
    return render(request, 'main/index.html', context=context)

def show(request, slug):
    news = get_object_or_404(News, slug=slug)
    rightBarNews = News.objects.all().order_by('date')

    context = {
        'rightBarNews': rightBarNews,
        'news': news,
        'menu': menu,
    }
    return render(request, 'main/post.html', context=context)

def world(request):
    rightBarNews = News.objects.all().order_by('date')
    content = News.objects.filter(categoryKey_id=1)

    context = {
        'content': content,
        'menu': menu,
        'rightBarNews': rightBarNews,
    }
    return render(request, 'main/newsSection.html', context=context)

def sport(request):
    rightBarNews = News.objects.all().order_by('date')
    content = News.objects.filter(categoryKey_id=2)

    context = {
        'content': content,
        'menu': menu,
        'rightBarNews': rightBarNews,
    }
    return render(request, 'main/newsSection.html', context=context)

def culture(request):
    rightBarNews = News.objects.all().order_by('date')
    content = News.objects.filter(categoryKey_id=3)

    context = {
        'content': content,
        'menu': menu,
        'rightBarNews': rightBarNews,
    }
    return render(request, 'main/newsSection.html', context=context)

def economic(request):
    rightBarNews = News.objects.all().order_by('date')
    content = News.objects.filter(categoryKey_id=4)

    context = {
        'content': content,
        'menu': menu,
        'rightBarNews': rightBarNews,
    }
    return render(request, 'main/newsSection.html', context=context)

def cinema(request):
    rightBarNews = News.objects.all().order_by('date')
    content = News.objects.filter(categoryKey_id=5)

    context = {
        'content': content,
        'menu': menu,
        'rightBarNews': rightBarNews,
    }
    return render(request, 'main/newsSection.html', context=context)

def exclusive_news(request):
    rightBarNews = News.objects.all().order_by('date')
    content = News.objects.filter(categoryKey_id=6)

    context = {
        'content': content,
        'menu': menu,
        'rightBarNews': rightBarNews,
    }
    return render(request, 'main/newsSection.html', context=context)

def about(request):
    rightBarNews = News.objects.all().order_by('date')

    context = {
        'rightBarNews': rightBarNews,
        'menu': menu,
    }
    return render(request, 'main/about.html', context=context)


