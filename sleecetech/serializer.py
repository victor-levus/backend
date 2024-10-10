from rest_framework import serializers

from sleecetech.models import Message


class SleeceMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 'created_at']

