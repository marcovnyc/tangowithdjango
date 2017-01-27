from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return HttpResponse("Rango says there world!")

def about(request):
    return HttpResponse("About this page")
