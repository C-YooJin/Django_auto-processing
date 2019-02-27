from django.http import HttpResponse
from django.shortcuts import render

def crawler(request):
    # return HttpResponse('여기는 말이지 크롤링을 하는 페이지야')
    return render(request, 'crawler/crawler_google.html')


# Create your views here.
