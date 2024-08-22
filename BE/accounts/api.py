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
    
#로그인/ 로그아웃
class AuthAPI (APIView):
    # 로그인
    def post(self, request):
    	# 유저 인증
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
        )
        # 이미 회원가입 된 유저일 때
        if user is not None:
            serializer = LoginSerializer(user)
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # 로그아웃
    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = Response({
            "message": "Logout success"
            }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response

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
                    "message": "register successs",
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
