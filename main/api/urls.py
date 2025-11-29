from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


from main.api import views

app_name = 'api'

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),  # noqa
    path('v1/', include(arg=[
        path('user/profile/', views.UserProfileAPIView.as_view(), name='user_profile_api'),

        path('auth/token/', views.AuthTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('auth/token/refresh/', views.AuthTokenRefreshView.as_view(), name='token_refresh'),
        path('auth/token/verify/', views.AuthTokenVerifyView.as_view(), name='token_verify'),
    ])),
    path('health_check', view=views.HealthCheckAPIView.as_view(), name="health_check"),
]
