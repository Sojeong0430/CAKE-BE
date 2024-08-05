from django.urls import path
from cakes.views import myroom_own , cake_custom ,myroom_visitor,message_open,create_message
app_name = 'cakes'

urlpatterns = [
    path('ownroom/<int:user_id>/',myroom_own,name='ownroom'),
    path('cakecustom/<int:user_id>/',cake_custom,name='cakemaker'),
    path('visit/<int:user_id>/',myroom_visitor,name='visitor'),
    path('message_open/<int:user_id>/',message_open,name='message_open'),
    path('createmessage/<int:user_id>/',create_message,name='messagemaker'),
    ]