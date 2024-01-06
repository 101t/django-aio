# -*- encoding: utf-8 -*-
from django.urls import path

from main.notify import views

app_name = 'notify'

urlpatterns = [
    path('manage/', views.notify_manage, name='notify_manage'),
    path('<str:request_type>/<str:slug>/', views.notify_detail, name='notify_detail'),
    path('', views.notify_list, name='notify_list'),
]
