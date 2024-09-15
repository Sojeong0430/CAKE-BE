from django.urls import path
from cakes.views import myroom_own , cake_custom ,myroom_visitor,message_open,create_message

from .api import CreateMessageAPI , DeleteMessageAPI , MessageListAPI , MessageRetieve , CakeCustomAPI ,CakeGetAPI , CakeGetVisitAPI , MessageCountAPI_owner , MessageCountAPI_visit

app_name = 'cakes'

urlpatterns = [
    path('ownroom/<int:user_id>/',myroom_own,name='ownroom'),
    path('cakecustom/<int:user_id>/',cake_custom,name='cakemaker'),
    path('visit/<int:user_id>/',myroom_visitor,name='visitor'),
    path('message_open/<int:user_id>/',message_open,name='message_open'),
    path('createmessage/<int:user_id>/',create_message,name='messagemaker'),

    #api
    path('api/createmessage/<str:user_name>/',CreateMessageAPI.as_view()), #메시지작성
    path('api/deletemessage/<int:message_id>/',DeleteMessageAPI.as_view()), #메시지삭제
    path('api/messagelist',MessageListAPI.as_view()), #메시지 리스트 조회
    path('api/messageretrieve/<int:message_id>/',MessageRetieve.as_view()), #메시지 detail 조회 
    path('api/cake-custom/',CakeCustomAPI.as_view()), #케이크 디자인 변경
    path('api/getcake/',CakeGetAPI.as_view()), #케이크 디자인 조회 (owner)
    path('api/getcakevisit/<str:owner_username>/',CakeGetVisitAPI.as_view()), #케이크 디자인 조회 (visit)
    path('api/messagecount_owner/',MessageCountAPI_owner.as_view()), #받은 메시지 갯수 조회 (owner)
    path('api/messagecount_visit/<str:user_name>/',MessageCountAPI_visit.as_view()), #받은 메시지 갯수 조회 (visit)
    ]