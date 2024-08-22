from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer1 , UserSerializer2 , LoginSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from birthday_cake.settings import SECRET_KEY
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer , TokenRefreshSerializer
import jwt

#유저 조회(pk,아이디,생년월일,케이크 몇 조각 쌓였는지)
class RetrieveUserAPI (APIView):

    permission_classes = [AllowAny]

    def get (self,request,user_id):

        try:
            User = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error':'해당하는 유저가 존재하지 않습니다'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer1(User)
        return Response(serializer.data)
    
#로그인
class AuthAPI (APIView):

    def post(self,request):
        user =  authenticate( #일치하면 사용자객체 반환 / 않으면 'None'반환
            username = request.data.get("username"),
            password = request.data.get("password")
        )

        if user is not None:
            serializer = UserSerializer2(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "로그인 성공",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response({'error':'로그인 실패'},status=status.HTTP_400_BAD_REQUEST)

#회원가입
class SignupAPI (APIView):

    def post(self, request):
        serializer = UserSerializer2(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "회원가입 성공",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True) #XSS공격 방지
            res.set_cookie("refresh", refresh_token, httponly=True) #xss공격 방지
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#로그아웃
class LogoutAPI (APIView):
    pass

#회원탈퇴
class AccountDeleteAPI (APIView):
    pass

#프로필 수정
class UpdateProfileAPI (APIView):
    pass
