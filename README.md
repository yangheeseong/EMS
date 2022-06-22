# EMS
###오류 로그 수집 시스템 - Toy Projects #1<br>
Sentry같은 오류 로그 수집 시스템이 지원되지 않는 곳에 사용하기 위해서 개발<br>
### 개발 스펙
Python, Django, Sqlite3, PostgreSQL, Btoostrap, AWS, Gunicorn, Nginx, Docker, Sentry
***
### <장고 프로젝트 기본 설정 및 실행 테스트 - 22.06.22>
>1.가상환경 설정 
> >File -> Project Structure -> SDKs -> Add New SDK -> Add Python SDK -> Virtualenv Environment 설정

>2.프로젝트 설정
> >File -> Project Structure -> Project -> SDK 설정

>3.가상환경 실행 
> >venv/Scripts/activate

>4.장고 4.0.3 설치 설치 
> >pip install django==4.0.3

>5.pip upgrade 
> >python -m pip install --upgrade pip

>6.장고 프로젝트 생성 (해당 프로젝트 디렉토리 이동)
> >django-admin startproject config .

>7.기본 설정 변경 
> >LANGUAGE_CODE = 'ko-kr' / TIME_ZONE = 'Asia/Seoul'

>8.장고 프로젝트 실행 (실행 테스트)
> >python manage.py runserver
***
### <ems App 생성 및 작동 테스트 - 22.06.22>
> python manage.py startapp ems
- config/urls.py 설정
<pre><code>
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ems/', include('ems.urls')),
]
</code></pre>
- ems/urls.py 생성 및 설정
<pre><code>
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
</code></pre>

- ems/views.py 테스트 코드 생성 및 작동 확인
<pre><code>
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")
</code></pre>
***