from django import forms
from memo.models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['memoName', 'memo']
        labels = {
            'memoName': '메모명',
            'memo': '메모',
        }