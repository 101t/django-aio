from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.contrib import messages

from main.core.utils import display_form_validations
from main.users.models import User
from main.users.forms import SignUpForm


def create_an_account(request):
    form = SignUpForm()
    if request.POST:
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User.objects.create_user(
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                email=email,
                username=email,
            )
            user.set_password(password)
            user.save()
            messages.success(request, _("Registration success"), extra_tags="success")
        else:
            display_form_validations(form=form, request=request)
    return render(request, "auth/signup.html", dict(form=form))
