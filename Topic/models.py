from django.db import models
from django.contrib.auth.models import User, auth


# Create your models here.

#-------------------------------------------------------------------------------------

class Topic(models.Model):
    # A Topic the user is learning about
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, parent_link=True)
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to='imgs/', default='imgs/default_topic.jpg')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

#-------------------------------------------------------------------------------------

class Entry(models.Model):
    # Entry the user creates for particular topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return f'{self.text[:50]}...'
    
#-------------------------------------------------------------------------------------

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.FileField(upload_to='imgs/', default='imgs/default_profile.jpg')
    bio = models.TextField(default='Your Bio Shows Up Here!')
    
    def __str__(self):
        return "%s's Profile" %self.user.username
    
    
#-------------------------------------------------------------------------------------

class Subscribe(models.Model):
    email = models.EmailField(max_length=254)
    
    def __str__(self):
            return self.email