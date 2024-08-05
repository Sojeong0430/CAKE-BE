from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    d_day = models.DateField()
    party_room_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
