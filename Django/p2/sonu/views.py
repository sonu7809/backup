from django.shortcuts import render
from .models import Student
# Create your views here.
def stud(request):
    stu=Student.objects.all()
    return render(request,'sonu/studetails.html',{'st':stu})
