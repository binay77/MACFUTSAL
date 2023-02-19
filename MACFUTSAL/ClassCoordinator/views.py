"""
from django.shortcuts import render
from . forms import AddForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from ClassCoordinator.models import Team_Registration
# Create your views here.

class Team_Registration(CreateView):
    model = Team_Registration
    from_class = AddForm
    template_name = 'Team_Registration.html'
    success_url = '/Team_Registration/'
    """

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.views.generic import View


class ClassCoordinatorView(UserPassesTestMixin, View):
    def test_func(self):
        user_groups = [group.name for group in self.request.user.groups.all()]
        return 'Class Coordinator' in user_groups

    def handle_no_permission(self):
        return render(self.request, 'Class_Coordinator views/forbidden.html')
    
    def get(self, request, *args, **kwargs):
        return render(request, 'Class_Coordinator views/Class_Coordinator_Views.html')