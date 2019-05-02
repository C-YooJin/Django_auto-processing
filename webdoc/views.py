# 임시
from django.shortcuts import render

def webdoc(request):
    # firstpages = firstpage.objects.all()
    return render(request, 'webdoc/webdoc.html')
