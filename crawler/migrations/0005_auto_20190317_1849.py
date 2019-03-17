# Generated by Django 2.1.7 on 2019-03-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0004_auto_20190317_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flickr_crawl',
            name='keyword',
            field=models.CharField(help_text='keyword to crawl images from google. ex) dog', max_length=100),
        ),
        migrations.AlterField(
            model_name='flickr_crawl',
            name='max_num',
            field=models.CharField(help_text='Number of images to download. 500이상 입력해주세요. ex) 10', max_length=50),
        ),
        migrations.AlterField(
            model_name='instagram_crawler',
            name='max_num',
            field=models.CharField(help_text='Number of images to download. ex) 10000', max_length=50),
        ),
    ]
