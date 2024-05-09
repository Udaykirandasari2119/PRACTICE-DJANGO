from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def secondFunction(request):
    return HttpResponse('second app is recived')