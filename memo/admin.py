from django.contrib import admin
from .models import Memo


# 검색 기능 추가
class MemoAdmin(admin.ModelAdmin):
    search_fields = ['memo']

# 테이블 관리 추가
admin.site.register(Memo, MemoAdmin)
