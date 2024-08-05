from django.db import models
from accounts.models import CustomUser
# Create your models here.

class message (models.Model):
    party = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_content = models.TextField()

