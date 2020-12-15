from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, HttpResponse

import json


def welcome_view(request):
    import django, sys
    python_version = "{}.{}.{}".format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
    return render(request, "web/welcome.html", dict(
        django_version=django.get_version(),
        python_version=python_version,
        platform=sys.platform,
    ))


def global_manage(request):
    args, res_status, res_message = {}, 400, _("Sorry, Command does not matched.")
    if request.GET and request.is_ajax():
        s = request.GET.get("s")
    if isinstance(args, dict):
        args["status"] = res_status
        args["message"] = str(res_message)
    else:
        res_status = 200
    return HttpResponse(json.dumps(args), status=res_status, content_type="application/json")
