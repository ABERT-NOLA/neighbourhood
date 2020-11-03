from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class User(AbstractUser):
    is_hood_admin = models.BooleanField(default=False)
    is_hood_member = models.BooleanField(default=False)

class HoodAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=255, default='071234567')

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=255, default='071234567')
    location = models.CharField(max_length=255)
    image= models.ImageField(blank=True, upload_to='photos', default='default.jpg')


class HoodAdminProfile(models.Model):
    user = models.OneToOneField(HoodAdmin, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, **kwargs):
        super().save()

class MemberProfile(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, **kwargs):
        super().save()
