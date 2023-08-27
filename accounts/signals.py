from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        default_group = Group.objects.get(name='default_group')
        if instance.is_superuser == False:
            instance.groups.add(default_group)
            instance.save()
            print('worked---')
    print('signal recieved---')