from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserSerializer1 (serializers.ModelSerializer):
    class Meta :
        model = CustomUser
        fields = ['id','username','birthday','pieces']

class UserSerializer2 (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','email','birthday')

        def create(self,validated_data): #새로운 사용자 객체를 생성할때 호출된다
            user = CustomUser.objects.create_user(
                username=validated_data['username'],
                password= validated_data['password'],
                email = validated_data['email'],
                birthday = validated_data['birthday'],
            )
            return user
        
class LoginSerializer (serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return data