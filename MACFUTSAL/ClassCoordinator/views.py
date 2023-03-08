from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.views.generic import View
from login.models import Profile



class ClassCoordinatorView(UserPassesTestMixin, View):
    def test_func(self):
        user_groups = [group.name for group in self.request.user.groups.all()]
        return 'Class Coordinator' in user_groups

    def handle_no_permission(self):
        return render(self.request, 'Class_Coordinator views/forbidden.html')
    
    def get(self, request, *args, **kwargs):
    
        current_user_profile = request.user.profile
        print(current_user_profile)
        # Get all profiles with the same batch value as the current user
        profiles = Profile.objects.filter(batch=current_user_profile.batch).exclude(user=request.user)
        context = { 
            'profiles': profiles
        }
        return render(request, 'Class_Coordinator views/Class_Coordinator_Views.html' , context )
    





