from django.urls import path
from . import views
from .api import FriendAddAPI , FriendListAPI , FriendDeleteAPI

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),  # 친구 목록 페이지
    path('add/', views.add_contact, name='add_contact'), # 친구 추가 페이지

    #api
    path('api/add-friend/<int:owner_id>',FriendAddAPI.as_view()),
    path('api/friends-list/<int:owner_id>',FriendListAPI.as_view()),
    path('api/delete-friend/<int:friend_id>',FriendDeleteAPI.as_view())

]