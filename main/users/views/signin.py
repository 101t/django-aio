from django.utils.translation import ugettext as _
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, render, redirect

from main.users.forms import SignInForm
from main.core.utils import display_form_validations


def signin_view(request):
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


def signout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
