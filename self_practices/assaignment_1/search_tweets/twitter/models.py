from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField(max_length=240)
    image = models.ImageField(upload_to='media/twitter/tweets/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text[:20]}'
