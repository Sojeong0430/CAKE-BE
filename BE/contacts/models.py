from django.db import models
from accounts.models import CustomUser

class Contact(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    birthday = models.DateField(null=False)
    party_room_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username

#https://도메인/partyroom/<username> << 주인(A) 입장에서의 파티룸 주소
#https://도메인/partyroom/<username>/visit << 방문자 입장에서의 A의 파티룸 주소
#http://localhost:3000