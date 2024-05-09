from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Department
from django.db.models import Sum,Avg,Min,Max

# Create your views here.

def dbprocessing(request):
    if request.method == 'POST':
        eno = int(request.POST['eno'])
        ename = (request.POST)['ename']
        esal = int(request.POST['esal'])
        dno = int(request.POST['dno'])
        
        dept = Department.objects.filter(deptno=dno)
        if len(dept)>0:
            emp = Employee(empno=eno,empname=ename,salary=esal,department=dept[0])
            emp.save()
            return HttpResponse('Inserted successfully')
        else:
            return HttpResponse('Department is no exisited')
    depts = Department.objects.all()
    return render(request,'DbApp/insert.html',{'depts':depts})

def selectEmployee(request):
    #emps = Employee.objects.all()
    emps = Employee.objects.select_related('department')
    total_salary = Employee.objects.aggregate(Sum('salary'))['salary__sum']
    avg_salary  = Employee.objects.aggregate(avg_sal=Avg('salary'))['avg_sal']
    min_salary = Employee.objects.aggregate(min_sal=Min('salary'))['min_sal']
    max_salary = Employee.objects.aggregate(max_sal=Max('salary'))['max_sal']



    return render(request,'DbApp/select.html',{'data':emps,'total_salary':total_salary,'avg_salary':avg_salary,'min_salary':min_salary,'max_salary':max_salary})

def detailEmployee(request,eno):
    if request.method == 'POST':
        eno = int(request.POST['t1'])
        ename = request.POST['t2']
        esal = int(request.POST['t3'])
        emp = Employee(empno=eno,empname=ename,salary=esal)
        emp.save()
        return redirect('selecturl')
    
    emp = Employee.objects.filter(empno=eno)
    return render(request,'DbApp/detail.html',{'data':emp})

def deleteEmployee(request,eno):
    emp = Employee.objects.get(empno=eno)
    emp.delete()
    return redirect('selecturl')


