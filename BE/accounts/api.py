from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer2 , RetrieveSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from birthday_cake.settings import SECRET_KEY
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer , TokenRefreshSerializer
import jwt
from rest_framework.permissions import AllowAny #실험용
from rest_framework_simplejwt.tokens import RefreshToken

# 유저 정보 확인
class RetrieveUserAPI (APIView):

    def get(self, request):
        try:
            # access token을 decode 해서 유저 id 추출 => 유저 식별
            access = request.COOKIES['access']
            payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
            pk = payload.get('user_id')
            user = get_object_or_404(CustomUser, pk=pk)
            serializer = RetrieveSerializer(instance=user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except(jwt.exceptions.ExpiredSignatureError):
            # 토큰 만료 시 토큰 갱신
            data = {'refresh': request.COOKIES.get('refresh', None)}
            serializer = TokenRefreshSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                access = serializer.data.get('access', None)
                refresh = serializer.data.get('refresh', None)
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(CustomUser, pk=pk)
                serializer = RetrieveSerializer(instance=user)
                res = Response(serializer.data, status=status.HTTP_200_OK)
                res.set_cookie('access', access)
                res.set_cookie('refresh', refresh)
                return res
            raise jwt.exceptions.InvalidTokenError

        except(jwt.exceptions.InvalidTokenError):
            # 사용 불가능한 토큰일 때
            return Response({'error':'사용불가능한 토큰입니다.'},status=status.HTTP_400_BAD_REQUEST)
    
#로그인
class AuthAPI (APIView):

    permission_classes = [AllowAny]
    
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
            res.set_cookie("access", access_token, httponly=True) #XSS공격 방지
            res.set_cookie("refresh", refresh_token, httponly=True) #xss공격 방지
            return res
        else:
            return Response({'error':'로그인 실패'},status=status.HTTP_400_BAD_REQUEST)

#로그아웃 : 토큰 삭제
class LogoutAPI(APIView):

    def delete(self,request):
        response = Response({'message':'로그아웃 성공'},status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response


#회원가입
class SignupAPI (APIView):

    permission_classes = [AllowAny]

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
    
#회원탈퇴
class AccountDeleteAPI (APIView):

    def post(self, request):

        user =  authenticate( #일치하면 사용자객체 반환 / 않으면 'None'반환
            username=request.user.username,
            password = request.data.get("password")
        )

        if user is not None:
            try:
                user = request.user
                user.delete()  # 사용자 삭제
                response = Response({'message': '탈퇴 완료'}, status=status.HTTP_200_OK)
                
                # 쿠키에서 JWT 토큰 삭제
                response.delete_cookie('access')
                response.delete_cookie('refresh')
                
                return response
            
            except Exception as e:
                return Response({'error': '탈퇴에 실패했습니다.', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message':'비밀번호가 틀렸습니다.'},status=status.HTTP_403_FORBIDDEN)