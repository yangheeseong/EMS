from django.urls import path

from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.memo, name='memo'),
    path('create/', views.create, name='create'),
    path('modify/<int:memo_id>/', views.modify, name='modify'),
    path('delete/<int:memo_id>/', views.delete, name='delete'),
]
