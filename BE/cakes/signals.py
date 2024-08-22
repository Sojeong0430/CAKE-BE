from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import cake_custom

@receiver(post_save, sender=CustomUser)
def User_save(sender,created,instance,**kwargs):
    print('created : ',created)
    if created:
        cake_custom.objects.create(party=instance)