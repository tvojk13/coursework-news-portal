from django.shortcuts import render
import datetime
from .models import *

def index(request):
    content = News.objects.all()
    return render(request, 'main/index.html', {'content': content}) # .strftime('%H:%M')
