from django.forms import ModelForm
from .models import google_crawl

class google_crawl_form(ModelForm):
    class Meta:
        model = google_crawl
        fields = ['name', 'employee number', 'team name', 'download data type', 'crawl contents', 'keyword', 'max num']