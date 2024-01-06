from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('jet/dashboard/', include('jet.dashboard.urls', namespace="jet-dashboard")),
    path('jet/', include('jet.urls', namespace="jet")),
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/', include('main.api.urls', namespace="api")),
    path('account/', include('main.users.urls', namespace="users")),
    path('notification/', include('main.notify.urls'), name='notify'),
    path('', include('main.web.urls', namespace="web")),
]
urlpatterns += (
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
