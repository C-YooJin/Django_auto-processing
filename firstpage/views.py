from django.http import HttpResponse


def first_page(request):
    return HttpResponse('이곳은 첫 번째 페이지! 왼쪽에 메뉴 바 만들어야됨')
# Create your views here.
