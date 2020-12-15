from django.urls import path

from .views import *

app_name = 'web'

urlpatterns = [
    path('manage/', global_manage, name='global_manage'),
    path('', welcome_view, name='welcome_view'),
]
