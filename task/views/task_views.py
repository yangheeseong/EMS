import logging

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from ..forms import TaskForm
from ..models import Task

logger = logging.getLogger('task')

def task(request):
    page = request.GET.get('page', '1')
    state = request.GET.get('state', 'N')
    kw = request.GET.get('kw', '')
    pageLength = request.GET.get('pageLength', '10')
    task_list = Task.objects.order_by('-createDate')

    if kw:
        task_list = task_list.filter(
            Q(taskName__icontains=kw)
        ).distinct()

    if state:
        task_list = task_list.filter(
            Q(completeState__icontains=state)
        ).distinct()

    paginator = Paginator(task_list, pageLength)
    page_obj = paginator.get_page(page)
    context = {'task_list': page_obj, 'page': page, 'kw': kw, 'pageLength': pageLength, 'state': state}

    return render(
        request,
        'task/task_list.html',
        context
    )


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    commentList = task.taskcomment_set.all

    context = {'task': task, 'commentList': commentList}

    return render(
        request,
        'task/task_detail.html',
        context
    )


@login_required(login_url='common:login')
def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()

            return redirect('task:task')
    else:
        form = TaskForm()

    context = {'form': form}

    return render(
        request,
        'task/task_form.html',
        context
    )


@login_required(login_url='common:login')
def modify(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.user != task.author:
        messages.error(request, '수정권한이 없습니다.')

        return redirect('task:detail', task_id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('task:detail', task_id=task_id)
    else:
        form = TaskForm(instance=task)

    context = {'form': form}

    return render(
        request,
        'task/task_form.html',
        context
    )


@login_required(login_url='common:login')
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.user != task.author:
        messages.error(request, '삭제권한이 없습니다.')

        return redirect('task:detail', task_id=task_id)

    task.delete()

    return redirect(
        'task:task'
    )
