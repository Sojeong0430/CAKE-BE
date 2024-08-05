from django.urls import path
from . import views
app_name = 'contacts'

urlpatterns = [
     path('', views.contact_list, name='contact_list'),  # 친구 목록 페이지
    path('add/', views.add_contact, name='add_contact'), # 친구 추가 페이지
]