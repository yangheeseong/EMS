from django.contrib import admin
from .models import Task, TaskComment, SiteType, DeviceType, Manager

# 검색 기능 추가
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['taskName']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment']

class SiteTypeAdmin(admin.ModelAdmin):
    search_fields = ['siteType']

class DeviceTypeAdmin(admin.ModelAdmin):
    search_fields = ['deviceType']

class ManagerAdmin(admin.ModelAdmin):
    search_fields = ['manage']

# 테이블 관리 추가
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment, CommentAdmin)
admin.site.register(SiteType, SiteTypeAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(Manager, ManagerAdmin)
