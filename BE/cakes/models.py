from django.db import models
from accounts.models import CustomUser
# Create your models here.

class message (models.Model):
    party = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_content = models.TextField()

class cake_custom (models.Model):
    base = models.CharField(max_length=100)
    decorations = models.CharField(max_length=100)
    syrup = models.CharField(max_length=100)

class message_cutom (models.Model):
    font = models.CharField(max_length=100)
    BG_image = models.CharField(max_length=100)
    space = models.CharField(max_length=100)