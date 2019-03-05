from django.http import HttpResponse
from django.shortcuts import render
from .models import Google_crawl
from .forms import GoogleForm
from django.views.generic import CreateView

# Create your views here.

class RequestCreateView(CreateView):
    model = Google_crawl
    form_class = GoogleForm
    template_name = 'crawler/crawler_google.html'

#def crawler_google(request):
 #   return render(request, 'crawler/crawler_google.html')

def crawler_flickr(request):
    return render(request, 'crawler/crawler_flickr.html')

def crawler_instagram(request):
    return render(request, 'crawler/crawler_instagram.html')

