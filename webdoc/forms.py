from django import forms
from .models import webdoc
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class WebdocForm(forms.ModelForm):

    class Meta:
        model = webdoc
        field = ('name', 'employee_number', 'team_name', 'domain_for_data', 'crawl_information')
        exclude = ('request_id', 'request_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Let\'s Request!'))