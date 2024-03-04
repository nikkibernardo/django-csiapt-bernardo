from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Welcome to Index Page!")

def contact(request):
    return HttpResponse("Contact Us Bitch!!!!!!")

##def vision(request):
##    return HttpResponse("CCMS Vision")

##def objective(request):
##    return HttpResponse("CCMS Objective")
