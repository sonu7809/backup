from django.shortcuts import render

# Create your views here.
def read(request):
    return render(request,'python.html') 