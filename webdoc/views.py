from .models import webdoc
from .forms import WebdocForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.core.mail import send_mail
import subprocess
import os

# 다국어 추가한부분 (모듈)
from django.utils import translation
from django.http import HttpResponse, JsonResponse

class WebdocCreateView(SuccessMessageMixin, CreateView):
    model = webdoc
    form_class = WebdocForm
    template_name = 'webdoc/webdoc.html'
    success_url = reverse_lazy('webdoc')
    success_message = "your request was sent successfully. We'll let you know by email when the crawling is complete. You can download your data from the CDL."

    def form_valid(self, form):
        send_mail(
            subject='[수집웹문서] {}님의 요청'.format(form.cleaned_data['name']),  # mail title
            message='{}팀의 {}님께서 데이터를 요청했습니다. 요청 정보: {}'
                .format(form.cleaned_data['team_name'], form.cleaned_data['name'],
                        form.cleaned_data['max_num'], form.cleaned_data['crawl_information']),  # mail contents
            # from_email='yoojin.choi@navercorp.com',  # from
            # recipient_list=['yoojin.choi@navercorp.com'],  # to
            from_email='yoojin31222@gmail.com',  # from
            recipient_list=['yoojin31222@gmail.com'],  # to
            fail_silently=False,
        )
        return super(WebdocCreateView, self).form_valid(form)

