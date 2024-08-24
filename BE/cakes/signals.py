from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import cake_custom

#user 생성되면 케이크 커스텀 모델 자동 생성
@receiver(post_save, sender=CustomUser)
def User_save(sender,created,instance,**kwargs):
    print('created success : ',created)
    if created:
        cake_custom.objects.create(party=instance)