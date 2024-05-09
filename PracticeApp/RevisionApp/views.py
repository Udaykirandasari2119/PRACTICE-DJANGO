from django.shortcuts import render,redirect
from DbApp.models import Employee

# Create your views here.

def selectData(request):
    emps = Employee.objects.all()
    return render(request,'RevisionApp/select.html',{'data':emps})

def insertData(request):
    if request.method == 'POST':
        eno = int(request.POST['t1'])
        ename = request.POST['t2']
        esal = int(request.POST['t3'])
        Employee.objects.create(empno=eno,empname=ename,salary=esal)
        return redirect('selectrevurl')
    
    return render(request,'RevisionApp/insert.html')

def updateData(request,eno):
    if request.method == 'POST':
        eno = int(request.POST['t1'])
        ename = request.POST['t2']
        esal = int(request.POST['t3'])

        emp = Employee(empno=eno,empname=ename,salary=esal)
        emp.save()
        return redirect('selectrevurl')
    
    emp = Employee.objects.get(empno=eno)
    return render(request,'RevisionApp/update.html',{'employee':emp}) 

def deleteData(request,eno):
    emp = Employee.objects.get(empno=eno)
    emp.delete()
    return redirect('selectrevurl')
