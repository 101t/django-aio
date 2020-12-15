from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from main.notify.models import Notification, NotificationRequest
from main.core.utils import get_query, paginate

import json

PER_PAGE = 25


@login_required
def notify_list(request):
    queryset = Notification.objects.filter(user=request.user).order_by("-created")
    q = request.GET.get("q")
    if q:
        entry_query = get_query(q, ("title", "body",))
        queryset = queryset.filter(entry_query)
    queryset = paginate(queryset, per_page=PER_PAGE, page=request.GET.get("page", 1))
    template_name = 'web/notify-list.html'
    return render(request, template_name, dict(queryset=queryset))


@login_required
def notify_detail(request, requesttype="", slug=""):
    obj = get_object_or_404(NotificationRequest, slug=slug, requesttype=requesttype)
    template_name = 'web/notify-detail.html'
    return render(request, template_name, dict(obj=obj))


@login_required
def notify_manage(request):
    args, res_status, res_message = {}, 400, _("Sorry, Command does not matched.")
    if request.GET and request.is_ajax():
        s = request.GET.get("s")
        if s == "all":
            queryset = Notification.objects.filter(user=request.user, read=False).order_by("-created")[:10]
            args = list(map(lambda a: a.get_small_dict(), queryset))
        elif s == "markall":
            Notification.objects.filter(user=request.user).update(read=True)
            res_message = _("All Notifications are marked as read")
            res_status = 200
        elif s == "mark":
            Notification.objects.filter(user=request.user).filter(pk__in=request.GET.getlist("pk")).update(read=True)
            obj = Notification.objects.filter(pk__in=request.GET.getlist("pk")).first()
            if obj:
                args["href"] = obj.href
            res_message = _("This Notification marked as read")
            res_status = 200
        elif s == "unmark":
            Notification.objects.filter(user=request.user).filter(pk__in=request.GET.getlist("pk")).update(read=False)
            obj = Notification.objects.filter(pk__in=request.GET.getlist("pk")).first()
            if obj:
                args["href"] = obj.href
            res_message = _("This Notification marked as unread")
            res_status = 200
    if isinstance(args, dict):
        args["status"] = res_status
        args["message"] = str(res_message)
    else:
        res_status = 200
    return HttpResponse(json.dumps(args), status=res_status, content_type="application/json")
