
"""
from django.urls import path
from .views import Team_Registration
app_name = 'ClassCoordinator'

urlpatterns = [
    path('ClassCoordinator/', Team_Registration.as_view(), name='add'),
    
]
"""

from django.urls import path
from .views import ClassCoordinatorView

urlpatterns = [
    path('BatchAdmin/', ClassCoordinatorView.as_view() , name='BatchAdmin'),
]