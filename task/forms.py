from django import forms
from task.models import Task, TaskComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ['comment']
        labels = {
            'comment': 'comment',
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['siteType', 'deviceType', 'prioritize', 'request', 'manager', 'taskName', 'referenceUrl', 'taskContent', 'completeState']
        labels = {
            'siteType': '사이트 구분',
            'deviceType': '기기 구분',
            'prioritize': '우선순위',
            'request': '요청자',
            'manager': '담당자',
            'taskName': '업무명',
            'referenceUrl': '참조URL',
            'taskContent': '내용',
            'completeState': '상태',
        }
