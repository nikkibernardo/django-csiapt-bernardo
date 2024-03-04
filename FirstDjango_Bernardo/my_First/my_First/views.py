from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Welcome to Index Page!")

def mission(request):
    return HttpResponse("CCMS Mission")

def vision(request):
    return HttpResponse("CCMS Vision")

def objective(request):
    return HttpResponse("CCMS Objective")
