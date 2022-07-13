from django import forms
from task.models import TaskComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ['comment']
        labels = {
            'comment': 'comment',
        }