from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from accounts.models import CustomUser
from .serializers import FriendADDSerializer, FriendListSerializer
from rest_framework.permissions import AllowAny #일시적으로 인증 비활성화, 개발 중에만 사용

#친구 추가 API 
class FriendAddAPI (APIView):

    def post(self,request):

        Owner = request.user
        
        serializer_username = FriendADDSerializer(data=request.data)
        serializer_username.is_valid(raise_exception=True)
        Friend_username = serializer_username.validated_data['username']

        try:
            SEARCH_friend = CustomUser.objects.get(username = Friend_username)
        except CustomUser.DoesNotExist :
            return Response({'error':'해당하는 친구가 존재하지 않습니다'},status=status.HTTP_404_NOT_FOUND)

        ADD_friend = Contact(
            owner = Owner,
            username=SEARCH_friend.username,
            birthday=SEARCH_friend.birthday,
            party_room_address = 'http://localhost:3000/'+SEARCH_friend.username+'/partyroom/visit'
        )
        ADD_friend.save()

        return Response({'success':'친구추가 성공'}, status=status.HTTP_201_CREATED)

#친구 리스트 조회 API
class FriendListAPI (APIView):

    #permission_classes = [AllowAny]
    def get (self,request):
        Owner = request.user
        queryset = Contact.objects.filter(owner=Owner)
        serializer = FriendListSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
#친구 삭제 API
class FriendDeleteAPI (APIView):
    
    #permission_classes = [AllowAny]

    def delete (self,request,friend_id):
        Owner = request.user
        try :
            friend = Contact.objects.get(id=friend_id)
        except Contact.DoesNotExist:
            return Response({'error':'해당하는 친구가 없습니다'},status=status.HTTP_404_NOT_FOUND)
        
        if friend.owner == Owner:
            friend.delete()
            return Response({'success':'친구 삭제 완료'},status=status.HTTP_204_NO_CONTENT)  
        else:
            return  Response({'message':'잘못된 접근입니다'},status=status.HTTP_403_FORBIDDEN)