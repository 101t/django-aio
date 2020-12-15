# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path

from main.notify.consumers import *

websocket_urlpatterns = [
    path('ws/session/<slug:session_id>/', SessionConsumer, name="session"),
    path('ws/broadcast/', BroadcastConsumer, name="broadcast"),
]
