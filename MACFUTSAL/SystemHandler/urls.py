
from django.urls import path

from SystemHandler.views import SystemHandlerView
#from SystemHandler.views import SystemHandlerView



urlpatterns = [
    path('SystemAdmin/', SystemHandlerView.as_view() , name='SystemAdmin'),
]