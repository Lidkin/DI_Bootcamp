from django.db.models.signals import post_save, pre_delete
from .models import Profile
from django.dispatch import receiver 

@receiver(post_save, sender=Profile)
def notify_new_profile(sender, instance, **kwargs):
    print(f'User: {instance.name} with email:{instance.email}')

@receiver(pre_delete, sender=Profile)   
def warn_before_deleting(sender, instance, **kwargs):
    if instance.is_active:
        print(f'{instance.name} still active!')
