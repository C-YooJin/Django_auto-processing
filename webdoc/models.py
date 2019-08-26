from django.db import models

# choice team name list
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

# choice Domain list
DOMAIN = (
    ('', 'please Choose Domain for crawl...'),
    ('instagram', 'instagram'),
    ('flickr', 'flickr'),
    ('500px', '500px')
)


class webdoc(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    employee_number = models.CharField(max_length=12, help_text='ex) KR62111')
    team_name = models.CharField(max_length=20, help_text='- TEAM NAME -', choices=TEAMS)
    domain_for_data = models.CharField(max_length=20, help_text=' - DOMAIN -', choices=DOMAIN)
    date_data_was_created = models.CharField(max_length=50, help_text='please write down a date that you want to crawl data ex) 20190101-20190102')
    crawl_information = models.TextField(max_length=100, help_text='Simply write down what research the data will be used in, please :)')
    request_date = models.DateTimeField(auto_now_add=True)


