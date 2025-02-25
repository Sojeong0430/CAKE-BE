from rest_framework import serializers
from .models import message , cake_custom

class MessageSerializer (serializers.ModelSerializer):
    class Meta:
        model = message
        fields=['pk','message_content','sent_by','font','matrix','background']
        read_only_fields = ['party']

class CakeSerializer (serializers.ModelSerializer):
    class Meta:
        model = cake_custom
        fields = "__all__"
        read_only_fields = ['party']
        
class MessageCountSerializer (serializers.Serializer):
     Message_count = serializers.IntegerField()