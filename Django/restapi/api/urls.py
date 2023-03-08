from django.urls import path,include
from django.contrib import admin
from api.views import companyviewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'companies',companyviewSet)

urlpatterns = [
    path('',include(router.urls))
    
]