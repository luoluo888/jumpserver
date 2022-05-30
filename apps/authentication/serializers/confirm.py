from rest_framework import serializers

from common.drf.fields import EncryptedField


class ConfirmSerializer(serializers.Serializer):
    method = serializers.CharField(required=True, max_length=64)
    secret_key = EncryptedField()
