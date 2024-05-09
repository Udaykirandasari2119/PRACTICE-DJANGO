from django.shortcuts import render

# Create your views here.

def firstFun(request):
    return render(request,'first.html')

def secondFun(request):
    return render(request,'second.html')
