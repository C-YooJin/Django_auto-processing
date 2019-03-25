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
            # Image_ONLY만 선택한 경우
            keyword = [x.strip() for x in keyword.split(',')]
            num = [x.strip() for x in num.split(',')]
            # save_dir = form.cleaned_data['name'] + '_' +form.cleaned_data['employee_number'] + '_' + form.cleaned_data['keyword']
            # save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
            for i in range(len(num)):
                num[i] = int(num[i])
            if len(keyword) > 1:
                for i in range(len(keyword)):
                    subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
                    save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[i])
                    save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
                    google_crawler_real(save, keyword[i], num[i], save_dir)
            else:
                subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
                save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[0])
                save = '/Users/user/Downloads/Google_crawling/unfiltered/{}'.format(save_dir)
                google_crawler_real(save, keyword[0], num[0], save_dir)                       # 수정포인트

        elif form.cleaned_data['download_type'] == '1':
            # META data 선택한 경우
            keyword = [x.strip() for x in keyword.split(',')]
            num = [x.strip() for x in num.split(',')]
            for i in range(len(num)):
                num[i] = int(num[i])
            if len(keyword) > 1:
                # if number of keyword is more than 1
                for i in range(len(keyword)):
                    subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
                    save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[i])
                    save = '/Users/user/Downloads/Google_crawling/meta/{}'.format(save_dir)
                    get_json(keyword[i], save, num[i], save_dir)
            else:
                # if number of keyword is 1
                subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
                save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[0])
                save = '/Users/user/Downloads/Google_crawling/meta/{}'.format(save_dir)
                get_json(keyword[0], save, num[0], save_dir)

        send_mail(
            subject= '[Google clawler] {}님의 크롤링 요청'.format(form.cleaned_data['name']),                        # mail title
            message= '{}팀의 {}님께서 {}, {}건에 대해 크롤링을 요청했습니다. 크롤링 정보: {}'
                .format(form.cleaned_data['team_name'], form.cleaned_data['name'], form.cleaned_data['keyword'], form.cleaned_data['max_num'], form.cleaned_data['crawl_info']),         # mail contents
            # from_email='yoojin.choi@navercorp.com',  # from
            # recipient_list=['yoojin.choi@navercorp.com'],  # to
            from_email='yoojin31222@gmail.com',          # from
            recipient_list=['yoojin31222@gmail.com'],   # to
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
        keyword = [x.strip() for x in keyword.split(',')]
        num = form.cleaned_data['max_num']
        num = [x.strip() for x in num.split(',')]
        # num str -> int
        for i in range(len(num)):
            num[i] = int(num[i])

        if len(keyword) > 1:
            # if number of keyword is more than 1
            for i in range(len(keyword)):
                subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
                save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[i])
                save = '/Users/user/Downloads/Flickr_crawling/{}'.format(save_dir)
                flickr_json(keyword[i], save, num[i], save_dir)
        else:
            subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # if number of keyword is 1
            save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number'] + '_{}'.format(keyword[0])
            save = '/Users/user/Downloads/Flickr_crawling/{}'.format(save_dir)
            flickr_json(keyword[0], save, num[0], save_dir)
        send_mail(
            subject='[Flickr clawler] {}님의 크롤링 요청'.format(form.cleaned_data['name']),  # mail title
            message='{}팀의 {}님께서 {}, {}건에 대해 크롤링을 요청했습니다. 크롤링 정보: {}'
                .format(form.cleaned_data['team_name'], form.cleaned_data['name'], form.cleaned_data['keyword'],
                        form.cleaned_data['max_num'], form.cleaned_data['crawl_info']),  # mail contents
            # from_email='yoojin.choi@navercorp.com',  # from
            # recipient_list=['yoojin.choi@navercorp.com'],  # to
            from_email='yoojin31222@gmail.com',  # from
            recipient_list=['yoojin31222@gmail.com'],  # to
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
        # extract keyword from db
        keyword = form.cleaned_data['keyword']

        # extract num from db
        num = form.cleaned_data['num']

        if form.cleaned_data['download_type'] == '0':  # choose Image only
            subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number']
            save = '/Users/user/Downloads/Instagram_crawling/Image/{}'.format(save_dir)
            run_image_only(keyword, num, save)

        elif form.cleaned_data['download_type'] == '1':  # choose json with meta info.
            subprocess.Popen(['python3', 'manage.py', 'process_tasks'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            save_dir = form.cleaned_data['name'] + '_' + form.cleaned_data['employee_number']
            save = '/Users/user/Downloads/Instagram_crawling/meta/{}'.format(save_dir)
            run_meta(keyword, num, save)

        send_mail(
            subject='[Instagram clawler] {}님의 크롤링 요청'.format(form.cleaned_data['name']),  # mail title
            message='{}팀의 {}님께서 {}, {}건에 대해 크롤링을 요청했습니다. 크롤링 정보: {}'.format(form.cleaned_data['team_name'],
                                                                            form.cleaned_data['name'],
                                                                            form.cleaned_data['keyword'],
                                                                            form.cleaned_data['num'],
                                                                            form.cleaned_data['crawl_info']),
            # from_email='yoojin.choi@navercorp.com',  # from
            # recipient_list=['yoojin.choi@navercorp.com'],  # to
            from_email='yoojin31222@gmail.com',  # from
            recipient_list=['yoojin31222@gmail.com'],  # to
            fail_silently=False,
        )
        return super(instagramcreateview, self).form_valid(form)
