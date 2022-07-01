from django import forms
from schedule.models import ScheduleComment


class ScheduleCommentForm(forms.ModelForm):
    class Meta:
        model = ScheduleComment
        fields = ['comment']
        labels = {
            'comment': 'comment',
        }