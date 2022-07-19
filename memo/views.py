import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import MemoForm
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


@login_required(login_url='common:login')
def create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)

        if form.is_valid():
            memo = form.save(commit=False)
            memo.author = request.user
            memo.save()

            return redirect('memo:memo')
    else:
        form = MemoForm()

    context = {'form': form}

    return render(
        request,
        'memo/memo_form.html',
        context
    )


@login_required(login_url='common:login')
def modify(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)

    if request.user != memo.author:
        messages.error(request, '수정권한이 없습니다.')

        return redirect('memo:memo')

    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)

        if form.is_valid():
            form.save()

            return redirect('memo:memo')
    else:
        form = MemoForm(instance=memo)

    context = {'form': form}

    return render(
        request,
        'memo/memo_form.html',
        context
    )


@login_required(login_url='common:login')
def delete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)

    if request.user != memo.author:
        messages.error(request, '삭제권한이 없습니다.')

        return redirect('memo:memo')

    memo.delete()

    return redirect(
        'memo:memo'
    )

