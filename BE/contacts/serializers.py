from rest_framework import serializers
from .models import Contact

class FriendADDSerializer (serializers.Serializer):
    username = serializers.CharField(max_length=150)

class FriendListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"