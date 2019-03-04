from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_post(request):
    return HttpResponse("I list!")
