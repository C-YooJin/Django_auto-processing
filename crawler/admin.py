from django.contrib import admin
from crawler.models import Google_crawl
# Register your models here.

class GoogleCrawlAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee_number', 'download_type', 'team_name', 'crawl_info', 'keyword', 'max_num',]
    readonly_fields = ('request_id','request_date',)

admin.site.register(Google_crawl, GoogleCrawlAdmin)