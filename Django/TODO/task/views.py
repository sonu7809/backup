from django.shortcuts import render,redirect
from . models import *
from . forms import *

# Create your views here.
def index(request):
    task=Task.objects.all()
    
    form= TaskForm()
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context ={'tasks':task,'form':form}
    return render(request, 'list.html',context)
