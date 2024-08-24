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
    decorations = models.IntegerField(default=0)
    syrup = models.IntegerField(default=0)