from django.db.models.signals import post_save
from .models import User, HoodAdmin, Member, MemberProfile, HoodAdminProfile
from django.dispatch import receiver

@receiver(post_save, sender=HoodAdmin)
def create_profile(sender, instance, created, **kwargs):
    if created:
        HoodAdminProfile.objects.create(user=instance)

@receiver(post_save, sender=HoodAdmin)
def save_profile(sender, instance, **kwargs):
    instance.hoodadminprofile.save()

@receiver(post_save, sender=Member)
def create_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)

@receiver(post_save, sender=MemberProfile)
def save_profile(sender, instance, **kwargs):
    instance.memberprofile.save()