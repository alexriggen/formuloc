from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length = 30,null = True)
    email = models.EmailField(unique = True)
    bio = models.TextField(null = True)
    
    avatar = models.ImageField(null = True, default="avatar.svg")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
class Formula(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    formula_text = models.TextField
    description = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-updated', '-created'] # - makes it go in descending order

    def __str__(self):
        return self.body[0:50] #outputs first 50 characters of body if only message is called
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE) #PARENT MODEL
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-updated', '-created'] # - makes it go in descending order

    def __str__(self):
        return self.body[0:50] #outputs first 50 characters of 