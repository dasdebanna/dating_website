from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Profile(models.Model):
    name = models.CharField(max_length=100)
    likes = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs ={'pk': self.pk})


class Request_To_Chat(models.Model):
  
    requestor = models.ForeignKey(Profile,on_delete=models.CASCADE, default= 2,related_name='%(class)s_requestor')#name2
    acceptor = models.ForeignKey(Profile,on_delete=models.CASCADE, default= 1,related_name='%(class)s_acceptor')#name1
    is_accepted = models.BooleanField(null=True)

     
    def __str__(self):

        return self.requestor.name + ' requested to chat with' + self.acceptor.name 

class Block(models.Model):
    person_blocked = models.CharField(max_length=100)
    blocked_by = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blocked_by + ' BLOCKED ' + self.person_blocked

class Room(models.Model):
    name = models.CharField(max_length=1000)
    

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True )
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)