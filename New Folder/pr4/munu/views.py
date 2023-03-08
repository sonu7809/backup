from django.shortcuts import render

# Create your views here.
def learn(request):
    data={'title':'python fees','pt':'python','fe':3000 }
    return render (request,'munu/munu1.html',data)
def read(request):
    note={'dj':'Django','fs':5000}
    return render (request,'munu/munu2.html',note)