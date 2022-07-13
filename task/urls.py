from django.urls import path

from .views import task_views, comment_views

app_name = 'task'

urlpatterns = [
    path('', task_views.task, name='task'),
    path('<int:task_id>/', task_views.detail, name='detail'),
    # path('update/<int:task_id>/<str:status>/', task_views.statusUpdate, name='statusUpdate'),
    path('comment/create/<int:task_id>/', comment_views.commentCreate, name='commentCreate'),
    path('comment/delete/<int:comment_id>/', comment_views.commentDelete, name='commentDelete')
]
