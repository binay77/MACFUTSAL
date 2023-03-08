from django.db import models
from django.contrib.auth.models import User, Group , Permission
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name = 'profile')
    token = models.CharField(max_length=150)
    verify = models.BooleanField(default=False)
    batch = models.CharField(max_length=4, blank=True, null=True)
    

    def __str__(self):
        return self.user.username


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group,related_name='roles')
    user_permissions = models.ManyToManyField(Permission , related_name='perms')
