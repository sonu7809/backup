from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Home Page')
def learn(request):
    return HttpResponse('Hello Django')
def fight(request):
    return HttpResponse('<h1>Hello Python</h1>')
def show(request):
    a=10+10
    return HttpResponse(a)
def hi(request):
    a='Hello sonu'
    return HttpResponse(a)
