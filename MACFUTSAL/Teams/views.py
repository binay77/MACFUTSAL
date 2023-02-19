from django.shortcuts import render
from django.http import HttpResponse

def Teams(request):
    
    return render(request,'Teams/Teams.html')