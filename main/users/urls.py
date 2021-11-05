# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.conf.urls import url
from django.urls import path, re_path
from .views import (
    profile_view,
    ResetPasswordRequestView, ResetPasswordConfirmView,
    signin_view,
    signout_view,
    create_an_account,
)

app_name = 'users'

urlpatterns = [
    path(route='signout/', view=signout_view, name="signout_view", ),
    path(route='profile/', view=profile_view, name="profile_view", ),
    path(route='create/', view=create_an_account, name="create_an_account", ),
    re_path(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', ResetPasswordConfirmView.as_view(),
            name='reset_confirm_view'),
    path(route='reset/', view=ResetPasswordRequestView.as_view(), name="reset_view", ),
    path(route='', view=signin_view, name="signin_view", ),
]
