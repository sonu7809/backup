from django.shortcuts import render

def home(request):
    dt={'sonu':'20000'}
    return render(request,'home.html',dt)