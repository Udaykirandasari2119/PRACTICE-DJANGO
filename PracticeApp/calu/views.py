from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calcufun(request):
    if request.method == 'POST':
        n1 = int(request.POST['t1'])
        n2 = int(request.POST['t2'])

        if 'add' in request.POST:
            res = n1+n2
            action = 'Addition'
        elif 'subs' in request.POST:
            res = n2-n1
            action = 'Subtraction'
        elif 'div' in request.POST:
            res = n2//n1
            action = 'Division'
        else:
            res = n1*n2
            action = 'Multiplication'
        return render(request,'cal.html',{'result':res,'action':action}) 
    return render(request,'cal.html')
