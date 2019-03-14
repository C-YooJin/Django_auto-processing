from .models import Google_crawl, flickr_crawl, instagram_crawler
from .forms import GoogleForm, flickrform
from django.views.generic import CreateView
from .download_google_images import google_crawler_real
from .download_flickr_json import flickr_json
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.core.mail import send_mail
import subprocess

class RequestCreateView(SuccessMessageMixin, CreateView):
    model = Google_crawl
    form_class = GoogleForm
    template_name = 'crawler/crawler_google.html'
    success_url = reverse_lazy('crawler_google')
    success_message = "your request was sent successfully. We'll let you know by email when the crawling is complete. You can download your data from the CDL."

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        keyword = [x.strip() for x in keyword.split(',')]
        num = form.cleaned_data['max_num']
        # save_dir = form.cleaned_data['name'] + '_' +form.cleaned_data['employee_number'] + '_' + form.cleaned_data['keyword']
        # save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
        subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if len(keyword) > 1:
            for i in range(len(keyword)):
                save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[i])
                save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
                google_crawler_real(save, keyword[i], num, save_dir)
        else:
            save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[0])
            save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
            google_crawler_real(save, keyword[0], num, save_dir)                       # 수정포인트
        send_mail(
            subject= '[Google clawler] {}님의 크롤링 요청'.format(form.cleaned_data['name']),                        # 메일 제목
            message= '{}팀의 {}님께서 {}, {}건에 대해 크롤링을 요청했습니다. 크롤링 정보: {}'
                .format(form.cleaned_data['team_name'], form.cleaned_data['name'], form.cleaned_data['keyword'], form.cleaned_data['max_num'], form.cleaned_data['crawl_info']),         # 메일 내용
            from_email='yoojin31222@gmail.com',          # 발신인
            recipient_list=['yoojin31222@gmail.com'],   # 수신인
            fail_silently=False,
        )
        return super(RequestCreateView, self).form_valid(form)


class flickrcreateview(SuccessMessageMixin, CreateView):
    model = flickr_crawl
    form_class = flickrform
    template_name = 'crawler/crawler_flickr.html'
    success_url = reverse_lazy('crawler_flickr')
    success_message = "your request was sent successfully. We'll let you know by email when the crawling is complete. You can download your data from the CDL."

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        num = form.cleaned_data['max_num']
        save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_' + form.cleaned_data[
            'keyword']
        save = '/Users/user/Downloads/Flickr_crawling/{}'.format(save_dir)
        subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        flickr_json(keyword, save, num)
        send_mail(
            subject='[Flickr clawler] {}님의 크롤링 요청'.format(form.cleaned_data['name']),  # 메일 제목
            message='{}팀의 {}님께서 {}, {}건에 대해 크롤링을 요청했습니다. 크롤링 정보: {}'
                .format(form.cleaned_data['team_name'], form.cleaned_data['name'], form.cleaned_data['keyword'],
                        form.cleaned_data['max_num'], form.cleaned_data['crawl_info']),  # 메일 내용
            from_email='yoojin31222@gmail.com',  # 발신인
            recipient_list=['yoojin31222@gmail.com'],  # 수신인
            fail_silently=False,
        )
        return super(flickrcreateview, self).form_valid(form)


def crawler_instagram(request):
    return render(request, 'crawler/crawler_instagram.html')

