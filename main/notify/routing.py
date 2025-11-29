"""WebSocket URL routing for notifications."""
from django.urls import path

from main.notify.consumers import BroadcastConsumer, SessionConsumer

websocket_urlpatterns = [
    path('ws/session/<slug:session_id>/', SessionConsumer.as_asgi(), name='session'),
    path('ws/broadcast/', BroadcastConsumer.as_asgi(), name='broadcast'),
]
