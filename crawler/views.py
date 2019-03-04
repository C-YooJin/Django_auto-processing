from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def crawler_google(request):
    return render(request, 'crawler/crawler_google.html')

def crawler_flickr(request):
    return render(request, 'crawler/crawler_flickr.html')

def crawler_instagram(request):
    return render(request, 'crawler/crawler_instagram.html')

