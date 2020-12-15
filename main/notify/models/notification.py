from django.utils.translation import ugettext_lazy as _
from django.db import models

from main.core.models import TimeStampedModel
from main.users.models import User

from autoslug import AutoSlugField


class Notification(TimeStampedModel):
    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ("-created",)

    fromuser = models.ForeignKey(User, verbose_name=_("From User"), null=True, blank=True,
                                 related_name='fromuser_notification', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    read = models.BooleanField(_("Is read"), default=False)
    title = models.CharField(_("Title"), max_length=255, )
    slug = AutoSlugField(populate_from='title', unique=True)
    body = models.TextField(_("Description"), )
    href = models.TextField(_("Extra Link"), blank=True)

    def __str__(self):
        return "{} > {}".format(self.title, self.user)

    def get_absolute_url(self):
        return self.href if self.href else "javascript:void(0)"

    @staticmethod
    def call_latest_notifications(user):
        notifications = Notification.objects.filter(user=user, read=False)
        for notify in notifications:
            notify.read = True
            notify.save()
        return notifications[:5]

    def get_dict(self):
        base_dict = TimeStampedModel.get_dict(self).copy()
        dic = {
            "pk": self.pk,
            "title": self.title,
            "slug": self.slug,
            "body": self.body,
            "href": self.get_absolute_url(),
            "read": self.read,
            "from_user": self.fromuser.get_dict() if self.fromuser else {},
            "user": self.user.get_dict() if self.user else {},
        }
        base_dict.update(dic)
        return base_dict

    def get_small_dict(self):
        base_dict = self.get_dict()
        del base_dict["from_user"]
        del base_dict["user"]
        return base_dict
