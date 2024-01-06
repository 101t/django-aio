from rest_framework import serializers


class HealthCheckSerializer(serializers.Serializer):
    version = serializers.CharField(max_length=255)
