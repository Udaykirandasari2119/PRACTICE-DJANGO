from django.shortcuts import render

# Create your views here.
def firstfunction(request):
    return render(request,'frt.html')

def secfunction(request):
    return render(request,'sec.html')