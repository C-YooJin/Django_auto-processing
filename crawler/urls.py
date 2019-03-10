from django.urls import path
from . import views
from crawler.views import RequestCreateView, flickrcreateview

urlpatterns = [
    path('google/', RequestCreateView.as_view(), name='crawler_google'),
    path('flickr/', flickrcreateview.as_view(), name='crawler_flickr'),
    path('instagram/', views.crawler_instagram, name='crawler_instagram'),
]