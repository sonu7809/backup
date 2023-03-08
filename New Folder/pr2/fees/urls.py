from django.urls import path
from . import views

urlpatterns = [
    path('lrn/',views.learn),
]