# MODEL 즉 테이블의 필드값을 지정해주는 파일
from django.utils.translation import ugettext_lazy as _
from django.db import models

TEAMS = (
    ('', 'Choose your team...'),
    ('NSML', 'NSML'),
    ('AI Production', 'AI Production'),
    ('AI Research', 'AI Research'),
    ('Biz AI', 'Biz AI'),
    ('OCR', 'OCR'),
    ('Speech', 'Speech'),
    ('Voice', 'Voice'),
    ('Vision', 'Vision'),
    ('Data & Connection', 'Data & Connection'),
    ('NSML Competition TF', 'NSML Competition TF'),
    ('DUET TF', 'DUET TF'),
    ('Pasha TF', 'Pasha TF')
)

JPG_YN = (
    ('0', 'Image Only'),
    ('1', 'JSON with meta information')
)


class Google_crawl(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=12, help_text='ex) KR62111')
    team_name = models.CharField(max_length=20, help_text='- TEAM NAME -', choices=TEAMS)
    download_type = models.CharField(max_length=20, choices=JPG_YN)       # Image only -> 0 / JSON with meta info. -> 1
    crawl_info = models.TextField(max_length=100, help_text='Simply write down what research the data will be used in.')
    keyword = models.CharField(max_length=100, help_text='Please enter the keyword for the data you want to crawl. You can enter multiple keyword using a comma. ex) green snake, pug')
    max_num = models.CharField(max_length=50, help_text='Number of images to download. Please enter max num value by the number of keywords you entered. ex) 500, 1000')
    request_date = models.DateTimeField(auto_now_add=True)

class flickr_crawl(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=12, help_text='ex) KR62111')
    team_name = models.CharField(max_length=20, help_text='- TEAM NAME -', choices=TEAMS)
    crawl_info = models.TextField(max_length=100, help_text='Simply write down what research the data will be used in.')
    keyword = models.CharField(max_length=100, help_text='Please enter the keyword for the data you want to crawl. You can enter multiple keyword using a comma. ex) green snake, pug')
    max_num = models.CharField(max_length=50, help_text='Number of images to download. Please enter 500 units. Please enter max num value by the number of keywords you entered. ex) 500, 1000')
    request_date = models.DateTimeField(auto_now_add=True)

class instagram_crawler(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=12, help_text='ex) KR62111')
    team_name = models.CharField(max_length=20, help_text='- TEAM NAME -', choices=TEAMS)
    download_type = models.CharField(max_length=20, choices=JPG_YN)  # Image only -> 0 / JSON with meta info. -> 1
    crawl_info = models.TextField(max_length=100, help_text='Simply write down what research the data will be used in.')
    keyword = models.CharField(max_length=100, help_text='Please enter the keyword for the data you want to crawl using space. ex) lovestagram greensnake')
    num = models.IntegerField(help_text='Number of images to download. All keywords can be crawled by the same number. Please enter only one number. ex) 500')
    #max_num = models.CharFiele(max_length=50, help_text='Number of images to download. Please enter max num value by the number of keywords you entered. ex) 1000, 5000')
    request_date = models.DateTimeField(auto_now_add=True)
