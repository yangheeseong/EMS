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
        fields = ['prioritize', 'request', 'taskName', 'referenceUrl', 'taskContent', 'completeState']
        labels = {
            'prioritize': '우선순위',
            'request': '요청자',
            'taskName': '업무명',
            'referenceUrl': '참조URL',
            'taskContent': '내용',
            'completeState': '상태',
        }
