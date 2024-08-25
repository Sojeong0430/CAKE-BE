from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class UserSerializer2 (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'birthday')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer2, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer2, self).update(instance, validated_data)

class LoginSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RetrieveSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"