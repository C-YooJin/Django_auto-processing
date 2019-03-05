from django import forms
from .models import Google_crawl
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.bootstrap import InlineRadios, Div
from crispy_forms.layout import Submit
#from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe


class GoogleForm(forms.ModelForm):
    #team_name = forms.ChoiceField(choices=TEAMS)
    #download_type = forms.TypedChoiceField(widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}), choices=URL_YN)

    class Meta:
        model = Google_crawl
        fields = ('name', 'employee_number', 'download_type', 'team_name', 'crawl_info', 'keyword', 'max_num')
        exclude = ('request_date', 'request_id')
        #widgets = {'download_type' : forms.RadioSelect()}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            #self.helper.layout = Layout(Div(InlineRadios('download_type')))
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Let\'s Crawl!'))