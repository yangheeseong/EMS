import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def mark(value):
    extensions = ['nl2br', 'fenced_code']

    return mark_safe(
        markdown.markdown(value, extensions=extensions)
    )


@register.filter
def completeStateText(value):
    if value == 'N':
        returnText = '준비'
    elif value == 'R':
        returnText = '기획검토'
    elif value == 'P':
        returnText = '진행'
    elif value == 'D':
        returnText = 'Dev 배포'
    elif value == 'S':
        returnText = 'Stage 배포'
    elif value == 'Q':
        returnText = 'QA'
    elif value == 'Y':
        returnText = '완료'
    elif value == 'E':
        returnText = '보류'

    return returnText
