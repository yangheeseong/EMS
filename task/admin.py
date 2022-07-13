from django.contrib import admin
from .models import Task, TaskComment


# 검색 기능 추가
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['taskName']

# 검색 기능 추가
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment']

# 테이블 관리 추가
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment, CommentAdmin)
