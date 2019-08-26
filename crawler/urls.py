from django.urls import path
from crawler.views import RequestCreateView, flickrcreateview, instagramcreateview

urlpatterns = [
    path('google/', RequestCreateView.as_view(), name='crawler_google'),
    path('flickr/', flickrcreateview.as_view(), name='crawler_flickr'),
    path('instagram/', instagramcreateview.as_view(), name='crawler_instagram'),
]