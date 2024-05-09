from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.

def display(request):
    if request.method == 'POST':
        #print(request)
        n1 = int(request.POST['t1'])
        n2 = int(request.POST['t2'])
        res = n1+n2
        return HttpResponse('addition is'+str(res))
    resp = render(request,'hello.html')
    return resp

