"""
from django.contrib import admin
from . import models


# Register your models here.
class SystemAdmin(admin.AdminSite):
    site_header = 'System Co-ordinator Area'

System_Coordinator_Site = SystemAdmin(name='SystemAdmin')

System_Coordinator_Site.register(models.Game_Updates)


admin.site.site_title = "MACFUTSAL Administration"
admin.site.site_header = "MACFUTSAL Administration"
admin.site.index_title = "MACFUTSAL User and Role Management"
"""
"""
from django.contrib import admin
from .models import Game_Updates

class Game_Updates_Admin(admin.ModelAdmin):
    pass

admin.site.register(Game_Updates, Game_Updates_Admin)
"""