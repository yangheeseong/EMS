import logging

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from ..models import SiteErrorLog

logger = logging.getLogger('ems')

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    pageLength = request.GET.get('pageLength', '10')
    log_list = SiteErrorLog.objects.order_by('-createDate')

    if kw:
        log_list = log_list.filter(
            Q(errorCategory__icontains=kw)
        ).distinct()

    paginator = Paginator(log_list, pageLength)
    page_obj = paginator.get_page(page)
    context = {'log_list': page_obj, 'page': page, 'kw': kw, 'pageLength': pageLength}

    return render(
        request,
        'ems/ems_list.html',
        context
    )


def detail(request, log_id):
    siteErrorLog = get_object_or_404(SiteErrorLog, pk=log_id)
    commentList = siteErrorLog.comment_set.all
    errorStatus = siteErrorLog.errorStatus

    btnResolveCss = 'btn btn-sm btn-outline-primary'
    btnIgnoreCss = 'btn btn-sm btn-outline-danger'

    if errorStatus == 'Resolve':
        btnResolveCss = 'btn btn-sm btn-primary'
        btnIgnoreCss = 'btn btn-sm btn-outline-danger'

    if errorStatus == 'Ignore':
        btnResolveCss = 'btn btn-sm btn-outline-primary'
        btnIgnoreCss = 'btn btn-sm btn-danger'

    context = {'log': siteErrorLog, 'commentList': commentList, 'btnResolveCss': btnResolveCss, 'btnIgnoreCss': btnIgnoreCss}

    return render(
        request,
        'ems/ems_detail.html',
        context
    )


@login_required(login_url='common:login')
def statusUpdate(request, log_id, status):
    siteErrorLog = get_object_or_404(SiteErrorLog, pk=log_id)
    errorStatus = siteErrorLog.errorStatus

    if not request.user.is_superuser:
        messages.error(request, '수정권한이 없습니다.')
    else:
        if errorStatus == status:
            updateStatus = None
        else:
            updateStatus = status

        siteErrorLog.errorStatus = updateStatus
        siteErrorLog.save()

    return redirect(
        'ems:detail',
        log_id=log_id
    )