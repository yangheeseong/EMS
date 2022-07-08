import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib import messages

from ..forms import CommentForm
from ..models import SiteErrorLog, Comment

logger = logging.getLogger('ems')

@login_required(login_url='common:login')
def commentCreate(request, log_id):
    siteErrorLog = get_object_or_404(SiteErrorLog, pk=log_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.siteErrorLog = siteErrorLog
            comment.save()

            return redirect('{}#comment_{}'.format(
                resolve_url('ems:detail', log_id=siteErrorLog.id), comment.id)
            )
    else:
        return HttpResponseNotAllowed('Only POST is possible.')


@login_required(login_url='common:login')
def commentDelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        comment.delete()

    return redirect(
        'ems:detail',
        log_id=comment.siteErrorLog.id
    )