from django.urls import path

from main.notify.views import *

app_name = 'notify'

urlpatterns = [
    path('manage/', notify_manage, name='notify_manage'),
    path('<str:requesttype>/<str:slug>/', notify_detail, name='notify_detail'),
    path('', notify_list, name='notify_list'),
]
