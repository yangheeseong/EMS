from django.urls import path

from .views import base_views


app_name = 'ems'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:log_id>/', base_views.detail, name='detail'),
    path('comment/create/<int:log_id>/', base_views.commentCreate, name='commentCreate')
]
