from django.shortcuts import render

# Create your views here.
def learn(request):
    return render(request,'django.html')