import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib import messages

from ..forms import CommentForm
from ..models import Task, TaskComment

logger = logging.getLogger('task')

@login_required(login_url='common:login')
def commentCreate(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = task
            comment.save()

            return redirect('{}#comment_{}'.format(
                resolve_url('task:detail', task_id=task.id), comment.id)
            )
    else:
        return HttpResponseNotAllowed('Only POST is possible.')

    context = {'task': task, 'form': form}

    return render(
        request,
        'task/task_detail.html',
        context
    )


@login_required(login_url='common:login')
def commentDelete(request, comment_id):
    comment = get_object_or_404(TaskComment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        comment.delete()

    return redirect(
        'task:detail',
        task_id=comment.task.id
    )
