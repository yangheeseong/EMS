from django.contrib import admin
from .models import Schedule, ScheduleComment


# 검색 기능 추가
class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ['taskName']

# 검색 기능 추가
class ScheduleCommentAdmin(admin.ModelAdmin):
    search_fields = ['comment']

# 테이블 관리 추가
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(ScheduleComment, ScheduleCommentAdmin)
