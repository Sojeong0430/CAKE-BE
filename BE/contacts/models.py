from django.db import models
from accounts.models import CustomUser

class Contact(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    birthday = models.DateField()
    d_day = models.IntegerField()
    party_room_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
