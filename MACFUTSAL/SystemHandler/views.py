
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.views.generic import View


class SystemHandlerView(UserPassesTestMixin, View):
    def test_func(self):
        user_groups = [group.name for group in self.request.user.groups.all()]
        return 'System Handler' in user_groups

    def handle_no_permission(self):
        return render(self.request, 'Class_Coordinator views/forbidden.html')
    
    def get(self, request, *args, **kwargs):
        return render(request, 'SystemHandler/System_Handler_Views.html')