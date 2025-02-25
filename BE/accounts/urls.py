from django.urls import path
from accounts.views import signup_view, login_view, logout_view
from .api import AuthAPI , SignupAPI , RetrieveUserAPI , AccountDeleteAPI , LogoutAPI
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    #api
    path('api/retrieveuser/',RetrieveUserAPI.as_view()),#유저 개별 조회
    path('api/signup/',SignupAPI.as_view()), #회원가입
    path("api/auth/",AuthAPI.as_view()), # 로그인
    path("api/logout/",LogoutAPI.as_view()),#로그아웃
    path("api/userdelete/",AccountDeleteAPI.as_view()), #회원탈퇴
    path("api/auth/refresh/",TokenRefreshView.as_view()), #jwt 토큰 재발급
]
