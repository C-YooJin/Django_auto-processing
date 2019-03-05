from django.db import models


TEAMS = (
    ('', 'Choose your team...'),
    ('1', 'NSML'),
    ('2', 'AI Production'),
    ('3', 'AI Research'),
    ('4', 'Biz AI'),
    ('5', 'OCR'),
    ('6', 'Speech'),
    ('7', 'Voice'),
    ('8', 'Vision'),
    ('9', 'Data & Connection'),
    ('10', 'NSML Competition TF'),
    ('11', 'DUET TF'),
    ('12', 'Pasha TF')
)


JPG_YN = (
    ('0', 'JPG_ONLY'),
    ('1', 'URL+Meta')
)

class Google_crawl(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, help_text='Name')
    employee_number = models.CharField(max_length=12, help_text='Employee Number ex) KR62111')
    team_name = models.CharField(max_length=20, help_text='- TEAM NAME -', choices=TEAMS)
    download_type = models.CharField(max_length=20, choices=JPG_YN)       # Image only -> 0 / url + meta info -> 1
    crawl_info = models.TextField(max_length=200, help_text='데이터가 어떤 연구 / 프로젝트에 사용 될지 말씀해주세요')
    keyword = models.CharField(max_length=20, help_text='keyword to crawl images from google ex) dog')
    max_num = models.IntegerField(help_text='Maximum number of images to download ex) 10000')
    request_date = models.DateTimeField(auto_now_add=True)

# Create your models here.
