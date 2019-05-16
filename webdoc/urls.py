from django.urls import path
from .views import WebdocCreateView
from . import views

urlpatterns = [
    path('', WebdocCreateView.as_view(), name='webdoc'),
]