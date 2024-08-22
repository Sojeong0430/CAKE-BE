from django.urls import path
from accounts.views import signup_view, login_view, logout_view
from .api import AuthAPI , SignupAPI , RetrieveUserAPI
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    #api
    path('api/retrieveuser/<int:user_id>/',RetrieveUserAPI.as_view()),
    path('api/signup/',SignupAPI.as_view()), #회원가입
    path("api/auth/",AuthAPI.as_view()), # 로그인
    path("api/auth/refresh/",TokenRefreshView.as_view()), #jwt 토큰 재발급
]
