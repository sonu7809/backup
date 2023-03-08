from django.urls import path
from . import views
urlpatterns = [
    path('rg/',views.show)
]
