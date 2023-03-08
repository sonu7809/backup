from django.urls import path
from . import views

urlpatterns = [
    path('fedj/',views.fees_dj),
    path('fepy/',views.fees_py)
]