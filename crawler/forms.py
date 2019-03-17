from django import forms
from .models import Google_crawl, flickr_crawl, instagram_crawler
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.bootstrap import InlineRadios, Div
from crispy_forms.layout import Submit
#from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe


# 크롤러 신청서 정보 저장
class GoogleForm(forms.ModelForm):

    class Meta:
        model = Google_crawl
        fields = ('name', 'employee_number', 'download_type', 'team_name', 'crawl_info', 'keyword', 'max_num')
        exclude = ('request_date', 'request_id')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Let\'s Crawl!'))


class flickrform(forms.ModelForm):
    class Meta:
        model = flickr_crawl
        fields = ('name', 'employee_number', 'team_name', 'crawl_info', 'keyword', 'max_num')
        exclude = ('request_date', 'request_id')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Let\'s Crawl!'))

class instagramform(forms.ModelForm):
    class Meta:
        model = instagram_crawler
        fields = ('name', 'employee_number', 'download_type', 'team_name', 'crawl_info', 'keyword', 'max_num')
        exclude = ('request_date', 'request_id')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Let\'s Crawl!'))
