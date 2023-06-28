from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news/<slug:slug>/', views.show, name='news'),
    path('world/', views.world, name='world'),
    path('sport/', views.sport, name='sport'),
    path('culture/', views.culture, name='culture'),
    path('economic/', views.economic, name='economic'),
    path('cinema/', views.cinema, name='cinema'),
    path('exclusive-news/', views.exclusive_news, name='exclusive-news'),
    path('about/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
