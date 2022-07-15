# EMS
### 오류 로그 수집 시스템 - Toy Projects #1<br>
오류 로그 수집 시스템이 지원되지 않는 곳에 사용하기 위해서 개발<br>
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
### <ems App 생성 및 실행 테스트 - 22.06.22>
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
### <DB Table 생성, Admin 추가 - 22.06.24>
- models.py 코드 작성 후 아래 명령어 실행
<pre><code>
python manage.py makemigrations
python manage.py migrate
</code></pre>
- Admin 관리자 생성
<pre><code>
python manage.py createsuperuser
</code></pre>
- Admin Table 관리기능과 검색 기능 추가
***
### <목록, 상세페이지 기능 추가. Bootstrap 적용 - 22.06.27>
- models.py Comment Class 추가
- 상세 페이지. 댓글 기능 추가
- Bootstrap 적용
- 목록 페이지. 페이징 추가
- 목록 페이지. 검색 추가
- 목록 페이지. 답변 갯수 표기
***
### <로그인, 로그아웃 추가 - 22.06.28>
- django.contrib.auth 사용
***
### <회원가입 및 편의 기능 추가 - 22.06.29>
- django.contrib.auth.forms 사용
- django.contrib.auth.models 사용
- 댓글 작성자 등록 추가 (모델 변경)
- 댓글 삭제 기능 추가
- markdown 추가
- SimpleMDE 적용
***
### <Docker, Gunicorn, Nginx, Postgres 설정 (AWS 배포)- 22.06.30>
- docker-compose. 개발, 배포용 생성
- nginx 관련 파일 생성
- .env. 개발, 배포용 생성
***
### <일정 관리 기능 추가 - 22.07.01>
- 간트차트 기능 추가
- 기존 Btoostrap CSS와 충돌 이슈로 새창으로 진행
***
### <ErrorLog 해결,무시 상태값 업데이트 기능 추가 - 22.07.08>
- 상세페이지 상태값 업데이트 기능 추가
***
### <업무 관리 기능 추가 - 22.07.12>
- app 생성
- config/settings INSTALLED_APPS 추가
- config/urls urlpatterns 추가
- models, urls, views 추가
***
### <업무 관리 기능 추가 - 22.07.13>
- 리스트, 상세페이지 생성
***
### <업무 관리 기능 추가 - 22.07.14>
- 수정, 삭제 기능 추가
***
### <업무 관리 기능 추가 - 22.07.15>
- 사이트구분, 디바이스타입, 담당자 Model 생성
- Task와 ManyToManyField로 정의