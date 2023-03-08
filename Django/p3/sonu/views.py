from django.shortcuts import render
from .forms import StudentRregistration
# Create your views here.
def show(request):
    fm=StudentRregistration()
    return render (request,'sonu/hi.html',{'form':fm})