from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    path('schedule/', views.schedule, name='schedule'),
    path('comment/create/<int:schedule_id>/', views.commentCreate, name='commentCreate'),
    path('comment/delete/<int:comment_id>/', views.commentDelete, name='commentDelete')
]
