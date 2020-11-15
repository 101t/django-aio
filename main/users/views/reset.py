from django.utils.translation import gettext as _
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.conf import settings
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from main.core.tasks import mail_html_maillist
from main.core.utils import display_form_validations
from main.users.forms import PasswordResetRequestForm, SetPasswordForm


class ResetPasswordRequestView(FormView):
    template_name = 'auth/reset.html'
    success_url = reverse_lazy("web:reset_view")
    form_class = PasswordResetRequestForm

    def post(self, request, *args, **kwargs):
        User = get_user_model()
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email_or_username"]
            try:
                user = User.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_url = reverse('web:reset_confirm_view', kwargs=dict(uidb64=uidb64, token=token))
                email_kwargs = dict(
                    email=user.email,
                    full_name=user.get_full_name(),
                    base_url=settings.BASE_URL,
                    site_name=settings.SITE_NAME,
                    reset_link=f"{settings.BASE_URL}{reset_url}",
                )
                subject = _("%(SITE_NAME)s Reset Password") % dict(SITE_NAME=settings.SITE_NAME)
                template = "email/reset_password_request.html"
                mail_html_maillist([user.email], subject=subject, html_template=template, kwargs=email_kwargs,
                                   lang=settings.LANGUAGE_CODE)
                messages.success(request, _("An email has been sent to %(email)s. Please check the inbox to continue "
                                            "resetting password") % dict(email=user.email))
                return self.form_valid(form=form)
            except (User.DoesNotExist, Exception) as e:
                messages.error(request, e)
        messages.error(request, _("Invalid Email Address"))
        return self.form_invalid(form=form)


class ResetPasswordConfirmView(FormView):
    template_name = 'auth/reset.html'
    success_url = reverse_lazy('web:signin_view')
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *args, **kwargs):
        User = get_user_model()
        form = self.form_class(request.POST)
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                password = form.cleaned_data["password"]
                user.set_password(password)
                user.save()
                email_kwargs = dict(
                    email=user.email,
                    full_name=user.get_full_name(),
                    base_url=settings.BASE_URL,
                    site_name=settings.SITE_NAME,
                )
                subject = _("%(SITE_NAME)s - Your Password has Changed") % dict(SITE_NAME=settings.SITE_NAME)
                template = "email/reset_password_information.html"
                mail_html_maillist([user.email], subject=subject, html_template=template, kwargs=email_kwargs,
                                   lang=settings.LANGUAGE_CODE)
                # TODO: Send email & notification information about password changes
                messages.success(request, _("Password has been reset successfully"))
                return self.form_valid(form)
            else:
                display_form_validations(form=form, request=request)
        else:
            messages.error(request, _("The password link is no longer valid."))
        return self.form_invalid(form=form)
