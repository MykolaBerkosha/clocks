
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)

    mobile = models.CharField(_('Mobile number'), max_length=255, blank=True)

    address = models.CharField(_('Address'), max_length=255, blank=True)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):

    if not hasattr(instance, 'profile'):
        UserProfile.objects.create(user=instance)
