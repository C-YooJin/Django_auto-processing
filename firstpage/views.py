from django.http import HttpResponse
from django.shortcuts import render
from .models import firstpage

def first_page(request):
    firstpages = firstpage.objects.all()
    return render(request, 'firstpage/index_real.html')
# Create your views here.
