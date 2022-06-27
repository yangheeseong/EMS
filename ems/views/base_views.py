from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from ..forms import CommentForm
from ..models import SiteErrorLog, Comment
from django.core.paginator import Paginator
from django.db.models import Q


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
    context = {'log': siteErrorLog}

    return render(
        request,
        'ems/ems_detail.html',
        context
    )


def commentCreate(request, log_id):
    siteErrorLog = get_object_or_404(SiteErrorLog, pk=log_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.siteErrorLog = siteErrorLog
            comment.save()

            return redirect(
                'ems:detail',
                log_id=log_id
            )
            # return redirect('{}#answer_{}'.format(
            #     resolve_url('pybo:detail', question_id=question.id), answer.id)
            # )
    else:
        return HttpResponseNotAllowed('Only POST is possible.')

    context = {'log': siteErrorLog, 'form': form}

    return render(
        request,
        'ems/ems_detail.html',
        context
    )
