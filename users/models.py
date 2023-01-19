from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#  Create your models here.

class Private_Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to = 'profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'


class Report(models.Model):
    reported = models.CharField(max_length=100)
    reported_by =  models.CharField(max_length=100, default= 'none')
    reason = models.TextField(default='none')
    
    def get_absolute_url(self):
        return reverse('meet-home')