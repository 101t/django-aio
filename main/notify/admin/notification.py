from django.contrib import admin

from ..models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "read", "created",)
    search_fields = ("title", "user__username", "user__first_name", "user__last_name", "user__email",)
    readonly_fields = ("read",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(NotificationAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False
