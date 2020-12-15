from django.conf import settings


def site(request):
    return {
        "SETTINGS": settings,
    }
