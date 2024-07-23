from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.

#생일 디데이 기능 구현하려면 user모델 수정해야함.
def myroom_own (request,user_id):
    owner = User.objects.get(id=user_id)
    context={'owner':owner}
    return render (request,'myroom/room_own.html',context)

def cake_custom (request):
    return render (request,'myroom/cakemaker.html')
