from django.urls import path

from .views import base_views, comment_views


app_name = 'ems'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:log_id>/', base_views.detail, name='detail'),
    path('log/update/<int:log_id>/<str:status>/', base_views.statusUpdate, name='statusUpdate'),
    path('comment/create/<int:log_id>/', comment_views.commentCreate, name='commentCreate'),
    path('comment/delete/<int:comment_id>/', comment_views.commentDelete, name='commentDelete')
]
