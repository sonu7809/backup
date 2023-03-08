from django.http import HttpResponse

def home(request):
    print("home")
    return HttpResponse("this is home page")
    