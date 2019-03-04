from django.forms import ModelForm
from .models import google_crawl

class GoogleCrawlForm(ModelForm):
    class Meta:
        model = google_crawl
        # fields = ['name', 'employee number', 'team name', 'download data type', 'crawl contents', 'keyword', 'max num']
        exlude = ['request_id', 'request_data']