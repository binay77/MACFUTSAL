"""
from django.contrib import admin
from . import models


# Register your models here.
class BatchAdmin(admin.AdminSite):
    site_header = 'Class Co-ordinator Area'

Class_Coordinator_Site = BatchAdmin(name='BatchAdmin')

Class_Coordinator_Site.register(models.Team_Registration)
"""

"""
from django.contrib import admin
from .models import Team_Registration

class Team_Registration_Admin(admin.ModelAdmin):
    pass

admin.site.register(Team_Registration, Team_Registration_Admin)
"""