from django.urls import path
from . import views
from crawler.views import RequestCreateView

urlpatterns = [
    path('google/', RequestCreateView.as_view(), name='crawler_google'),
    path('google/success/', RequestCreateView.as_view(), name = 'crawler_google_success'),
    path('flickr/', views.crawler_flickr, name='crawler_flickr'),
    path('instagram/', views.crawler_instagram, name='crawler_instagram'),
]