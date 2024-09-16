from django.db import models
from accounts.models import CustomUser
# Create your models here.

class message (models.Model):
    party = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_content = models.TextField()
    background = models.IntegerField(default=0)
    sent_by = models.CharField(max_length=225)
    font = models.IntegerField(default=0)
    matrix = models.IntegerField(default=0)

class cake_custom (models.Model):
    party = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    base = models.IntegerField(default=0)
    light= models.IntegerField(default=0)

    deco1 = models.IntegerField(default=0)
    deco2 = models.IntegerField(default=0)
    deco3 = models.IntegerField(default=0)
    deco4 = models.IntegerField(default=0)
    deco5 = models.IntegerField(default=0)
    deco6 = models.IntegerField(default=0)
    deco7 = models.IntegerField(default=0)
    deco8 = models.IntegerField(default=0)
    deco9 = models.IntegerField(default=0)
    deco10 = models.IntegerField(default=0)
    deco11 = models.IntegerField(default=0)
    