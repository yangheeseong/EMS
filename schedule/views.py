import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from .forms import ScheduleCommentForm
from .models import Schedule, ScheduleComment

logger = logging.getLogger('ems')

def schedule(request):
    schedule_id = request.GET.get('schedule_id', '1')
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule_comment = schedule.schedulecomment_set.all

    context = {'schedule': schedule, 'schedule_comment': schedule_comment}

    return render(
        request,
        'schedule/schedule.html',
        context
    )


@login_required(login_url='common:login')
def commentCreate(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    if request.method == 'POST':
        form = ScheduleCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.schedule = schedule
            comment.save()

            return redirect('{}#comment_{}'.format(
                resolve_url('schedule:schedule'), comment.id)
            )
    else:
        return HttpResponseNotAllowed('Only POST is possible.')

    context = {'schedule': schedule, 'form': form}

    return render(
        request,
        'schedule/schedule.html',
        context
    )


@login_required(login_url='common:login')
def commentDelete(request, comment_id):
    comment = get_object_or_404(ScheduleComment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        comment.delete()

    return redirect(
        'schedule:schedule'
    )