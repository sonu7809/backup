from django.urls import path
from . import views
urlpatterns = [
    path('tc/',views.teach),
    path('wk/',views.work),
]
