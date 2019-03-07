from django.http import HttpResponse
from django.shortcuts import render
from .models import Google_crawl
from .forms import GoogleForm
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from .download_google_images import google_crawler_real
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.contrib import messages

# Create your views here.

class RequestCreateView(SuccessMessageMixin, CreateView):
    model = Google_crawl
    form_class = GoogleForm
    template_name = 'crawler/crawler_google.html'
    success_url = reverse_lazy('crawler_google')
    success_message = "your request was sent successfully"

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        max_num = form.cleaned_data['max_num']
        save = '/Users/user/Downloads/new/'
        google_crawler_real(save, keyword, max_num)
        return super(RequestCreateView, self).form_valid(form)


def crawler_flickr(request):
    return render(request, 'crawler/crawler_flickr.html')

def crawler_instagram(request):
    return render(request, 'crawler/crawler_instagram.html')

