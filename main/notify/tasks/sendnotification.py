from django.utils.translation import gettext_lazy as _

from main.users.models import User
from config.celery import app
from config.constants import MAX_RETRIES, DEFAULT_RETRY_DELAY
from main.notify.models import Notification, NotificationRequest
from main.notify.livecast import send_to_session

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(bind=True, default_retry_delay=DEFAULT_RETRY_DELAY, max_retries=MAX_RETRIES)
def send_notification(self, userid, title, body, href):
    """
    Usage:
    >>> from main.notify.tasks import send_notification
    >>> send_notification.apply_async(kwargs=dict(userid=1, title="Test", body="description", href=None), countdown=1)
    """
    try:
        user = User.objects.get(pk=userid)
        data = dict(
            user=user,
            title=title,
            body=body,
        )
        if href:
            data["href"] = href
        Notification.objects.create(**data)
        send_to_session(caller=None, callee=user)
        self.update_state(state="SUCCESS")
    except User.DoesNotExist:
        self.update_state(state="FAILURE")


@app.task(bind=True, default_retry_delay=DEFAULT_RETRY_DELAY, max_retries=MAX_RETRIES)
def request_notification_task(self, request_notification_pk):
    try:
        request_notification = NotificationRequest.objects.get(pk=request_notification_pk)
    except NotificationRequest.DoesNotExist:
        return
    staff_only = request_notification.staff_only
    title = request_notification.title or str(_("New Notification"))
    notify_body = request_notification.body
    if staff_only:
        users = User.objects.filter(is_staff=True, is_active=True)
    else:
        users = User.objects.filter(is_active=True)
    users = users.distinct()
    request_notification.count = users.count()
    request_notification.save()
    for user in users:
        data = dict(
            title=title,
            body=notify_body,
            href=request_notification.get_absolute_url(),
            user=user,
        )
        Notification.objects.create(**data)
        send_to_session(caller=None, callee=user)
