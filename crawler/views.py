from .models import Google_crawl, flickr_crawl, instagram_crawler
from .forms import GoogleForm, flickrform, instagramform
from django.views.generic import CreateView
from .download_google_images import google_crawler_real
from .download_flickr_json import flickr_json
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.core.mail import send_mail
from .google_meta import get_json
from .instagram_run import run_image_only, run_meta
import subprocess
import os

class RequestCreateView(SuccessMessageMixin, CreateView):
    model = Google_crawl
    form_class = GoogleForm
    template_name = 'crawler/crawler_google.html'
    success_url = reverse_lazy('crawler_google')
    success_message = "your request was sent successfully. We'll let you know by email when the crawling is complete. You can download your data from the CDL."

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        num = form.cleaned_data['max_num']

        if form.cleaned_data['download_type'] == '0':
            # JPG_ONLY만 선택한 경우
            keyword = [x.strip() for x in keyword.split(',')]
            num = [x.strip() for x in num.split(',')]
            # save_dir = form.cleaned_data['name'] + '_' +form.cleaned_data['employee_number'] + '_' + form.cleaned_data['keyword']
            # save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
            for i in range(len(num)):
                num[i] = int(num[i])
            subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if len(keyword) > 1:
                for i in range(len(keyword)):
                    save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[i])
                    save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
                    google_crawler_real(save, keyword[i], num[i], save_dir)
            else:
                save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[0])
                save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
                google_crawler_real(save, keyword[0], num[0], save_dir)                       # 수정포인트

        elif form.cleaned_data['download_type'] == '1':
            # META data 선택한 경우
            subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            num = int(num)
            save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_' + form.cleaned_data['keyword']
            save = '/Users/user/Downloads/Google_crawling/meta/{}'.format(save_dir)
            get_json(keyword, save, num, save_dir)

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


class instagramcreateview(SuccessMessageMixin, CreateView):
    model = instagram_crawler
    form_class = instagramform
    template_name = 'crawler/crawler_instagram.html'
    success_url = reverse_lazy('crawler_instagram')
    success_message = "your request was sent successfully. We'll let you know by email when the crawling is complete. You can download your data from the CDL."

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        num = form.cleaned_data['max_num']
        save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_' + form.cleaned_data['keyword']
        save = "/Users/user/Downloads/Instagram_crawling/{}".format(save_dir)

        os.system('cd instagram-scraper/')

        # Crawling
        if form.cleaned_data['download_type'] == '0':         # choose Image only
            subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            run_image_only(keyword, num, save)
            # os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --maximum {} -d {}'.format(keyword, num, save))

        elif form.cleaned_data['download_type'] == '1':       # choose json with meta info.
            subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            run_meta(keyword, num, save)
            # os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --maximum {} -d {} --media-metadata'.format(keyword, num, save))

        send_mail(
            subject='[Instagram clawler] {}님의 크롤링 요청'.format(form.cleaned_data['name']),  # mail title
            message='{}팀의 {}님께서 {}, {}건에 대해 크롤링을 요청했습니다. 크롤링 정보: {}'
                .format(form.cleaned_data['team_name'], form.cleaned_data['name'], form.cleaned_data['keyword'],
                        form.cleaned_data['max_num'], form.cleaned_data['crawl_info']),  # mail contents
            from_email='yoojin31222@gmail.com',  # from
            recipient_list=['yoojin31222@gmail.com'],  # to
            fail_silently=False,
        )
        return super(instagramcreateview, self).form_valid(form)

