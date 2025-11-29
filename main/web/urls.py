# -*- encoding: utf-8 -*-
from django.urls import path

from main.web import views

app_name = 'web'

urlpatterns = [
    path('manage/', views.global_manage, name='global_manage'),
    path('', views.welcome_view, name='welcome_view'),
]
