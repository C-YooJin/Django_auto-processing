from django.db import models

class google_crawl(models.Model):
    name = models.CharField(max_length=20, help_text='Name')
    employee_number = models.CharField(max_length=12, help_text='Employee Number ex) KR62111', primary_key=True)
    team_name = models.CharField(max_length=20, help_text='- TEAM NAME -')
    download_type = models.IntegerField()       # Image only -> 0 / url + meta info -> 1
    crawl_info = models.TextField()
    keyword = models.CharField(max_length=20, help_text='keyword to crawl images from google ex) dog')
    max_num = models.IntegerField()

# Create your models here.
