from rest_framework import serializers
from messagess.models import Message

from django.core import signing


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'created', 'content']

    def validate_content(self, value):
        """ Encrypt content """
        if value:
            value = signing.dumps(value)
            return value

        return value