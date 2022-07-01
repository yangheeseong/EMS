from django.contrib import admin
from .models import SiteErrorLog, Comment


# 검색 기능 추가
class ErrorAdmin(admin.ModelAdmin):
    search_fields = ['errorCategory']

# 검색 기능 추가
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment']

# 테이블 관리 추가
admin.site.register(SiteErrorLog, ErrorAdmin)
admin.site.register(Comment, CommentAdmin)
