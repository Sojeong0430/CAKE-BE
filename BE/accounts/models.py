from django.contrib.auth.models import AbstractUser
from django.db import models
from birthday_cake import settings

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    pieces = models.IntegerField(default=0)