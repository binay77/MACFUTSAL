from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey( User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

class Application(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    batch = models.CharField(max_length=10)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name