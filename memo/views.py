import logging

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import Memo

logger = logging.getLogger('memo')

def memo(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    pageLength = request.GET.get('pageLength', '5')
    memo_list = Memo.objects.order_by('-createDate')

    if int(page) < 1:
        page = '1'

    if kw:
        memo_list = memo_list.filter(
            Q(memoName__icontains=kw) |
            Q(memo__icontains=kw)
        ).distinct()

    paginator = Paginator(memo_list, pageLength)
    page_obj = paginator.get_page(page)
    context = {'memo_list': page_obj, 'page': page, 'kw': kw, 'pageLength': pageLength}

    return render(
        request,
        'memo/memo_list.html',
        context
    )
