from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotifyConfig(AppConfig):
    name = "main.notify"
    verbose_name = _("Notifications")

    def ready(self):
        import main.notify.signals
