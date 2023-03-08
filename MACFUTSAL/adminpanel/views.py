from django.shortcuts import render,HttpResponse
from . models import Posts
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from login.models import Profile


# Create your views here.
from django.contrib.auth.decorators import user_passes_test


def admin_view(request):
    return render(request, 'adminpanel/Template/Admin/admin_view.html')


def Dashboard(request):
    return render(request,'adminpanel/Template/admin/Dashboard.html')


def post_page(request):
    form = PostForm()
    posts = Posts.objects.all()
    if request.method == "POST": 
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        "form":form,
        "posts":posts,
    }
    return render(request,'adminpanel/Template/admin/Posts_and_Updates.html',context)



def Roles(request):
    applications = Application.objects.all()
    return render(request, 'adminpanel/Template/Admin/Roles.html', {'applications': applications})


def Notices(request):
    return render(request, 'adminpanel/Template/Admin/Notices.html')

from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import StaffLoginForm


def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user and user.is_staff:
                login(request, user)
                #return redirect('admin_view')
                return render(request, 'adminpanel/Template/Admin/admin_view.html')
            else:
                #form.add_error(None, "Invalid username or password")
                return render(request, 'Class_Coordinator views/forbidden.html')
    else:
        form = StaffLoginForm()
    return render(request, 'adminpanel/Template/Admin/staff_login.html', {'form': form})
   
def delete_post(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)
        post.delete()
    except Posts.DoesNotExist:
        messages.error(request, "Post does not exist")
    return redirect('adminpanel:post_page')

def delete_Application_for_CR(request, application_id):
    try:
        application = Application.objects.get(id=application_id)
        application.delete()
    except Application.DoesNotExist:
        messages.error(request, "Application does not exist")
    return redirect('adminpanel:Roles')


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import Group, User
from .models import Application



def delete_Permission_for_CR(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    user = User.objects.get(email=application.email)
    user.groups.clear() # Remove user from all groups
    applications = Application.objects.filter(accepted=True)
    application.delete()
    return render(request, 'adminpanel/Template/Admin/UserManagement.html', {'applications': applications})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import Group , User
from .models import Application

def accept_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    application.accepted = True
    application.save()
    user = User.objects.get(email=application.email)
    group = Group.objects.get(name='Class Coordinator')
    user.groups.add(group)
    applications = Application.objects.filter(accepted=True)
    return render(request, 'adminpanel/Template/Admin/Roles.html', {'applications': applications})



from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Application

def UserManagement(request):
    applications = Application.objects.filter(accepted=True)
    return render(request, 'adminpanel/Template/Admin/UserManagement.html', {'applications': applications})



#handling  CR application form
from django.shortcuts import render
from .forms import ApplyForClassCoordinator
from . models import Application
# from django.contrib.auth.decorators import login_required


def CRform(request):
    submitted = False
    if request.method == 'POST':
        form = ApplyForClassCoordinator(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = ApplyForClassCoordinator()

    applications = Application.objects.all()

    context = {
        'form': form,
        'applications': applications,
        'submitted': submitted
    }
    return render(request, 'adminpanel/Template/admin/apply_for_class_coordinator.html', context)



def GM(request):
    return render(request, "GM/gm.html" )



def class_coordinator(request):
    # Get the current user's profile
    current_user_profile = request.user.profile

    # Get all profiles with the same batch value as the current user
    profiles = Profile.objects.filter(batch=current_user_profile.batch).exclude(user=request.user)
    
    # Render the template with the profiles
    return render(request, 'Class_Coordinator.html', {'profiles': profiles})