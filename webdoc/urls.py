from django.urls import path
from .views import webdoc

urlpatterns = [
    path('crawlrequest/', webdoc(), name='crawlrequest'),
]