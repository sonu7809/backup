from django.urls import path
from . import views

urlpatterns = [
    path('rd/',views.read ),
    
]