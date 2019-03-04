from django.urls import path
from . import views

urlpatterns = [
    path('google/', views.crawler_google, name='crawler_google'),
    path('flickr/', views.crawler_flickr, name='crawler_flickr'),
    path('instagram/', views.crawler_instagram, name='crawler_instagram'),
]