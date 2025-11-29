# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect, render, redirect
from django.utils.translation import gettext as _

from main.core.utils import display_form_validations
from main.users.forms import SignInForm


def login_view(request):
    form = SignInForm()
    if request.POST:
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            nextpage = request.POST.get("next") or "/"
            try:
                user = authenticate(email=username, username=username, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        if not user.is_email:
                            messages.warning(request, _(
                                "Your Email Address is not verified yet! please verify your email address."))
                        return redirect(nextpage)
                    else:
                        messages.warning(request, _('User banned, please contact support'))
                else:
                    raise Exception(_("Login Error, Invalid username or password, please try again"))
            except:
                messages.error(request, _('Login Error, Invalid username or password, please try again'))
        else:
            display_form_validations(form=form, request=request)
    return render(request, "auth/signin.html", dict(form=form))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
