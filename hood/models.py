from django.db import models
from users.models import User, Member
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    fire_dept = models.CharField(max_length=100, null=True)
    health_eme = models.CharField(max_length=100, null=True)
    police_cont = models.CharField(max_length=100, null=True)
    occ_count = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('admin_pr') 

    @classmethod
    def get_all_neighbourhoods(cls):
        return cls.objects.all()
    

class Business(models.Model):
    
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    desc = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('admin_pr') 

    @classmethod
    def get_all_businesses(cls):
        return cls.objects.all()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pics', default='default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('welcome-index') 

    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by('-date_posted')


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content