from django.urls import path
from . import views

urlpatterns = [
    path('lrndj/',views.learn_django ),
    path('lrnpy/',views.learn_python)
]
