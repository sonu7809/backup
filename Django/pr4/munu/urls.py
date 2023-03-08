from django.urls import path
from . import views

urlpatterns = [
    path('ln/',views.learn),
    path('rd/',views.read),
]
