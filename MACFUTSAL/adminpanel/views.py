from django.shortcuts import render,HttpResponse
from . models import Posts
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

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


def UserManagement(request):
    return render(request, 'adminpanel/Template/Admin/UserManagement.html')


def Roles(request):
    return render(request, 'adminpanel/Template/Admin/Roles.html')


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
