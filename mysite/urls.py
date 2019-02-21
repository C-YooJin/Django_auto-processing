"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

 URL 매핑은 path() 함수 list 변수인 urlpatterns 을 통해 관리됩니다.
 (번역자주: urlpattenr= [  path(...), path(...), path(...), path(...) ] 식으로).
 각각의 path() 함수는 패턴이 일치할 때 표시(displayed)될 지정된 뷰에 URL 패턴을 연결하거나, 다른 URL 패턴 테스트 코드 목록에 연결합니다
 (이 두 번째 경우에서 패턴은 대상 모듈에서 정의된 패턴의 "기본 URL"이 됩니다).
 urlpatterns 리스트는 맨 처음에 관리자 어플리케이션의 고유한 URL 매핑 정의를 갖고 있는 admin.site.urls 모듈에 admin/ 패턴을 가지고 있는 모든 URL을 매핑하는 단일 함수를 정의합니다.

"""
# from django.conf.urls import include
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('firstpage.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls'))
]
"""
