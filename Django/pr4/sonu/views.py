from django.shortcuts import render

# Create your views here.
def teach(request):
    
    
    return render (request,'sonu/sonu1.html',{'nm':'sonu'})

def work(request):
    return render (request,'sonu/sonu2.html',{'dt':'soumendra'})