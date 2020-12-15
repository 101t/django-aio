from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from main.core.utils import display_form_validations
from main.users.forms import ProfileForm


@login_required
def profile_view(request):
    form = ProfileForm(instance=request.user)
    if request.POST:
        form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request=request, message=_("Your profile has been updated successfully"))
        else:
            display_form_validations(form=form, request=request)
        return redirect(reverse("users:profile_view"))
    return render(request, "auth/profile.html", dict(form=form))
