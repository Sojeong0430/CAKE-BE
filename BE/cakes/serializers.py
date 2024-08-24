from rest_framework import serializers
from .models import message , cake_custom

class MessageSerializer (serializers.ModelSerializer):
    class Meta:
        model = message
        fields=['message_content','sent_by','font','matrix','background']
        read_only_fields = ['party']

class CakeSerializer (serializers.ModelSerializer):
    class Meta:
        model = cake_custom
        fields = ['base','decorations','syrup']
        read_only_fields = ['party']
