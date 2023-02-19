"""
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Team_Registration(models.Model):

    Team_Name = models.CharField(max_length=30)
    slug = models.SlugField(null=True)
    Team_Manager = models.CharField(max_length=50)
    Goal_Keeper = models.CharField(max_length=50)
    Striker_1 = models.CharField(max_length=50)
    Striker_2 = models.CharField(max_length=50)
    Defeander_1 = models.CharField(max_length=50)
    Defeander_2 = models.CharField(max_length=50)
    Subs_1 = models.CharField(max_length=50)
    Subs_2 = models.CharField(max_length=50)
    Subs_3 = models.CharField(max_length=50)
    Subs_4 = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
"""