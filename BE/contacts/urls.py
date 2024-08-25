from django.urls import path
from . import views
from .api import FriendAddAPI , FriendListAPI , FriendDeleteAPI

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),  # 친구 목록 페이지
    path('add/', views.add_contact, name='add_contact'), # 친구 추가 페이지

    #api
    path('api/add-friend/',FriendAddAPI.as_view()), #친구추가 API   
    path('api/friends-list/',FriendListAPI.as_view()), #친구 리스트 조회 API
    path('api/delete-friend/<int:friend_id>',FriendDeleteAPI.as_view()) #친구삭제 API
]