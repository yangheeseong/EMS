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
        fields = ['taskName',
                  'referenceUrl',
                  'siteType',
                  'deviceType',
                  'manager',
                  'request',
                  'prioritize',
                  'taskState',
                  'taskProgress',
                  'taskStartDate',
                  'taskEndDate',
                  'taskContent'
        ]
        labels = {
            'taskName': '업무명',
            'referenceUrl': '참조 URL',
            'siteType': '사이트 구분',
            'deviceType': '기기 구분',
            'manager': '담당자',
            'request': '요청자',
            'prioritize': '우선순위',
            'taskState': '상태',
            'taskProgress': '진행률',
            'taskStartDate': '시작일',
            'taskEndDate': '종료일',
            'taskContent': '내용',
        }
