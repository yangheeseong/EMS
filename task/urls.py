from django.urls import path

from .views import task_views, comment_views

app_name = 'task'

urlpatterns = [
    # task_view.py
    path('', task_views.task, name='task'),
    path('<int:task_id>/', task_views.detail, name='detail'),
    path('create/', task_views.create, name='create'),
    path('modify/<int:task_id>/', task_views.modify, name='modify'),
    path('delete/<int:task_id>/', task_views.delete, name='delete'),
    # path('update/<int:task_id>/<str:status>/', task_views.statusUpdate, name='statusUpdate'),
    # comment_view.py
    path('comment/create/<int:task_id>/', comment_views.commentCreate, name='commentCreate'),
    path('comment/delete/<int:comment_id>/', comment_views.commentDelete, name='commentDelete')
]
