from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', blank=True, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', blank=True, null=True)
    message = models.TextField() 
    date_posted = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.message[:50]}"

