from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Matrix!")

def about(request):
    return HttpResponse("The Matrix is a fake reality, do you want to take the blue or redpill?")
