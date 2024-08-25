from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import cake_custom , message
from accounts.models import CustomUser 
from rest_framework.permissions import AllowAny

#메시지 작성 API
class CreateMessageAPI(APIView): 

    permission_classes = [AllowAny]

    def post (self,request,user_id):

        try :
            party = CustomUser.objects.get(id=user_id)
        except :
            return Response({'error':'해당되는 파티가 존재하지 않습니다.'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save(party=party)
            return Response({'message':'축하 메시지 전송 완료'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#메시지 삭제 API    
class DeleteMessageAPI (APIView):

    def delete (self,request,message_id):

        Message = message.objects.get(pk=message_id)
        owner = request.user

        if Message.party == owner:
            try:
                Message = message.objects.get(pk=message_id)
            except message.DoesNotExist:
                return Response({"error":"해당하는 메시지가 존재하지 않습니다"},status=status.HTTP_404_NOT_FOUND)
            Message.delete()
            return Response({'message':'메시지 삭제 완료'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error':'잘못된 접근입니다'},status=status.HTTP_403_FORBIDDEN)

#메시지 목록 조회 API
class MessageListAPI (APIView):

    def get (self,request):
        owner = request.user
        message_list = message.objects.filter(party=owner)
        serializer = MessageSerializer(message_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#메시지 개별 조회 API 
class MessageRetieve(APIView):

    def get (self,request,message_id):
        owner = request.user
        try:
            Message = message.objects.get(pk=message_id)
        except message.DoesNotExist:
            return Response({"error":"해당하는 메시지가 존재하지 않습니다."},status=status.HTTP_404_NOT_FOUND)
        if Message.party == owner:
            serializer = MessageSerializer(Message)
            return Response(serializer.data)
        else:
            return Response({"message":"잘못된 접근입니다"},status=status.HTTP_403_FORBIDDEN)
    
#케이크 커스텀 API
class CakeCustomAPI (APIView): 

    def patch (self,request):
        owner = request.user
        try :
            cake = cake_custom.objects.get(party=owner)
        except cake_custom.DoesNotExist :
            return Response ({"error":"해당하는 케이크가 없습니다"},status=status.HTTP_404_NOT_FOUND)
        serializer = CakeSerializer(cake,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        cake = serializer.save()
        serializer = CakeSerializer(cake)
        return Response(serializer.data)
    
#케이크 디자인 불러오기 API (owner)    
class CakeGetAPI (APIView):

    def get (self,request):
        owner = request.user
        cake = cake_custom.objects.get(party=owner)
        serializer = CakeSerializer(cake)
        return Response (serializer.data)

#케이크 디자인 불러오기 API (visit)     
class CakeGetVisitAPI (APIView):

    permission_classes = [AllowAny]

    def get (self,request,owner_username):
        owner = CustomUser.objects.get(username=owner_username)
        cake = cake_custom.objects.get(party=owner)
        serializer = CakeSerializer(cake)
        return Response (serializer.data)
