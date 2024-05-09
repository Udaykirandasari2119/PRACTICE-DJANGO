from django.shortcuts import render

# Create your views here.
def dtlfunction(request):
    if request.method=='POST':
        name=request.POST['t1']
        return render(request,'dt.html',{'greeting':'hello','output':name})
    return render(request,'dt.html')