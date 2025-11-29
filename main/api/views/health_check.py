from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.api.constants import TAGS
from main.api.serializers import HealthCheckSerializer
from version import VERSION


class HealthCheckAPIView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = HealthCheckSerializer

    @extend_schema(tags=[TAGS.PREFERENCES], summary="Health check")
    def get(self, request):
        return Response(data={'version': VERSION}, status=status.HTTP_200_OK)
