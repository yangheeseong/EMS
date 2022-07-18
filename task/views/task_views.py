import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from ..forms import TaskForm
from ..models import Task, SiteType, DeviceType, Manager

logger = logging.getLogger('task')

def task(request):
    page = request.GET.get('page', '1')
    state = request.GET.get('state', 'N')
    kw = request.GET.get('kw', '')
    pageLength = request.GET.get('pageLength', '10')
    task_list = Task.objects.order_by('-createDate')

    if int(page) < 1:
        page = '1'

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
    siteTypeList = SiteType.objects.all
    deviceList = DeviceType.objects.all
    manageList = Manager.objects.all

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()

            # ManyToManyField insert는 .add를 사용
            for siteType in request.POST.getlist('siteType'):
                task.siteType.add(siteType)

            for deviceType in request.POST.getlist('deviceType'):
                task.deviceType.add(deviceType)

            for manager in request.POST.getlist('manager'):
                task.manager.add(manager)

            return redirect('task:task')
    else:
        form = TaskForm()

    context = {'form': form, 'siteTypeList': siteTypeList, 'deviceList': deviceList, 'manageList': manageList}

    return render(
        request,
        'task/task_form.html',
        context
    )


@login_required(login_url='common:login')
def modify(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    siteTypeList = SiteType.objects.all
    deviceList = DeviceType.objects.all
    manageList = Manager.objects.all

    if request.user != task.author:
        messages.error(request, '수정권한이 없습니다.')

        return redirect('task:detail', task_id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task = form.save(commit=False)
            # python -> json type 변경
            # task.siteType = json.dumps(request.POST.getlist('siteType'), ensure_ascii=False)
            # task.deviceType = json.dumps(request.POST.getlist('deviceType'), ensure_ascii=False)
            # task.manager = json.dumps(request.POST.getlist('manager'), ensure_ascii=False)

            # ManyToManyField update는 .set을 사용
            task.siteType.set(request.POST.getlist('siteType'))
            task.deviceType.set(request.POST.getlist('deviceType'))
            task.manager.set(request.POST.getlist('manager'))

            form.save()

            return redirect('task:detail', task_id=task_id)
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'task': task, 'siteTypeList': siteTypeList, 'deviceList': deviceList, 'manageList': manageList}

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
