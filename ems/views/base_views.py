import logging

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

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

    context = {'log': siteErrorLog, 'commentList': commentList}

    return render(
        request,
        'ems/ems_detail.html',
        context
    )
