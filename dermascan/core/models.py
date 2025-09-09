from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank= True, null= True)
    medical_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

#for IMage scans
class Scan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "scans")
    image = models.ImageField(upload_to="scans/")
    result = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scan by {self.user.username} on {self.created_at}"

#Chat history

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} at {self.created_at}"