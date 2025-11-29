# -*- encoding: utf-8 -*-
from django.urls import path, re_path

from .views import (
    profile_view,
    ResetPasswordRequestView, ResetPasswordConfirmView,
    login_view,
    logout_view,
    create_an_account,
)

app_name = 'users'

urlpatterns = [
    path(route='logout/', view=logout_view, name="logout_view", ),
    path(route='profile/', view=profile_view, name="profile_view", ),
    path(route='create/', view=create_an_account, name="create_an_account", ),
    re_path(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', ResetPasswordConfirmView.as_view(),
            name='reset_confirm_view'),
    path(route='reset/', view=ResetPasswordRequestView.as_view(), name="reset_view", ),
    path(route='', view=login_view, name="login_view", ),
]
