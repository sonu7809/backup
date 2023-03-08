from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    cname='Python'
    duration='3 months'
    seats= 100
    django_dt={'nm':cname,'du':duration,'st':seats}
    
    return render(request,'course/courseone.html',context=django_dt)
def learn_python(request):
    return render(request,'course/coursetwo.html')