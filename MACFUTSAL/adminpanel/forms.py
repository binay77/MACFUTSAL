
from django import forms
from . models import Posts

class StaffLoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"

        
from .models import Application

class ApplyForClassCoordinator(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'phone', 'batch']
        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone',
            'batch': 'Batch'
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch'}),
        }