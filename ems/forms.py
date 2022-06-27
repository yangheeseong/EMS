from django import forms
from ems.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': 'comment',
        }