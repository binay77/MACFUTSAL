# myproject/adminpanel/urls.py
from django.urls import path
from .views import  staff_login , admin_view , Dashboard , post_page , UserManagement , Roles, Notices
from . import views
from .views import delete_post
app_name = 'adminpanel'

urlpatterns = [
    path('adminpanel/admin_view', admin_view, name='admin_view'),
    path('adminpanel/', staff_login, name='staff_login'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('adminpanel/admin_view/Dashboard/', Dashboard, name='Dashboard'),
    path('adminpanel/admin_view/Posts/', post_page , name='post_page'),
    path('adminpanel/admin_view/UserManagement/', UserManagement, name='UserManagement'),
    path('adminpanel/admin_view/Roles/', Roles, name='Roles'),
    path('adminpanel/admin_view/Notices/', Notices, name='Notices'),
    
]
