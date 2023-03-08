from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from adminpanel.models import Posts
from adminpanel.forms import PostForm
#from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from.models import Profile
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from adminpanel.models import Messag
from login.models import Profile
from . models import CustomUser


def index(request):
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
    return render(request, 'Accounts/index.html', context)

def About(request):
    return render(request, "Accounts/About.html")

def Profile(request):
     return render(request, "Accounts/Profile.html" )

# def GM(request):
#     return render(request, "GM/gm.html" )


def Contact(request):
    return render(request, "Accounts/contacts.html")

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_object = User.objects.filter(username = username).first()
        if user_object is None:
            messages.success(request, 'User not found.')
            return redirect("LoginView")
        profile_object = Profile.objects.filter(user = user_object).first()
        if profile_object.verify == False:
            messages.success(request, 'Account not verified, check your mail.')
            return redirect("LoginView")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('LoginView')
        login(request, user)
        return redirect('index')
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        batch = request.POST.get('batch')
        password = request.POST.get('password')
        # print(username, email, password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is already taken.')
                return redirect('register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is already taken.')
                return redirect('register')

            # create a user object
            user_object = User.objects.create(username = username, email = email )
            user_object.set_password(password)
            user_object.save()

            token = str(uuid.uuid4())
            # create a profile object for that user
            profile_object = Profile.objects.create(user = user_object, token = token,  batch=batch)
            profile_object.save()

            send_mail_for_verification(email, token)

            return redirect("token_send")
        except Exception as e:
            print(e)


    return render(request, "Accounts/register.html")


def verification(request, token):
    try:
        profile_object = Profile.objects.filter(token = token).first()
        if profile_object:
            if profile_object.verify:
                messages.success(request, 'Your account is already verified.')
                return redirect("LoginView")
            profile_object.verify = True
            profile_object.save()
            messages.success(request, 'Congratulation, your account has been verified.')
            return redirect("LoginView")
        else:
            return redirect("/error")

    except Exception as e:
        print(e)
        return redirect("index")





    
def success(request):
    return render(request, "Accounts/success.html")

def token_send(request):
    return render(request, "Accounts/tokens_send.html")


def send_mail_for_verification(email, token):
    subject = "Your MacFutsal account needs to be verified!!"
    message = f"Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}"
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_form, recipient_list)

def error_page(request):
    return render(request, "error.html")



