from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.api.constants import TAGS
from main.users.models import User


class UserProfileAPIView(APIView):
    serializer_class = None

    @extend_schema(tags=[TAGS.USER], summary="Get user profile")
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        return Response(
            data={"user": user.get_dict()},
            status=status.HTTP_200_OK,
        )
