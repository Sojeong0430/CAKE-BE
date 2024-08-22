from django.db import models
from accounts.models import CustomUser
# Create your models here.

class message (models.Model):
    party = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_content = models.TextField()
    background = models.IntegerField(default=0)
    sent_by = models.CharField(max_length=10) #이거 빼기
    font = models.IntegerField(default=0)
    matrix = models.IntegerField(default=0)
    #background = 0
    # font 0-6 = 스타일1 / 1= 스타일2 / 2= 스타일3
    # matrix 0-6 = 가운데정렬 / 1 = 오른쪽 정렬 / 2 = 왼쪽정렬


class cake_custom (models.Model):
    party = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    base = models.IntegerField(default=0)
    decorations = models.IntegerField(default=0)
    syrup = models.IntegerField(default=0)