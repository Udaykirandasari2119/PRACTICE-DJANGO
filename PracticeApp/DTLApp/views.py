from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dtlFunction(request):
    if request.method == 'POST':
        name = request.POST['t1']
        return render(request,'dtl.html',{'greeting':'Hello','output':name})
    return render(request,'dtl.html')