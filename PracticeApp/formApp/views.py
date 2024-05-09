from django.shortcuts import render,redirect
from . forms import FirstForm,EmpForm,EmpmodelForm,RegisterForm
from DbApp.models import Employee,Department 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .decorators import checkSuperUser,checkGroup
from django.core.paginator import Paginator

# Create your views here.

def firstForm(request):
    emptyForm = FirstForm()
    if request.method == 'POST':
        dataForm = FirstForm(request.POST)
        if dataForm.is_valid() == True:
            name = dataForm.cleaned_data['name']
            age = dataForm.cleaned_data['age']
            doj = dataForm.cleaned_data['doj']
            return render(request,'formApp/firstForm.html',{'name':name,'age':age,'form':emptyForm,'doj':doj})
        else:
            print(dataForm.errors)
            return render(request,'formApp/firstForm.html',{'form':dataForm,'error':dataForm.errors})
    
    
    return render(request,'formApp/firstForm.html',{'form':emptyForm})  #This is Get request line code

def empinsert(request):
    emptyForm = EmpForm()  #empty form is the object
    
    if request.method == 'POST':
        dataForm = EmpForm(request.POST)
        if dataForm.is_valid() == True:
            eno = dataForm.cleaned_data['empno']
            ename = dataForm.cleaned_data['empname']
            esal = dataForm.cleaned_data['salary']
            edept = dataForm.cleaned_data['department']

            deptData=Department.objects.filter(deptno=edept)
            if len(deptData)>0:
                Employee.objects.create(empno=eno,empname=ename,salary=esal,department=deptData[0])
                messages.success(request,'Data inserted successfully')
                return render(request,'formApp/insert.html',{'form':emptyForm})
            else:
                messages.error(request,'Department is not avalible')
                return render(request,'formApp/insert.html',{'form':dataForm})

    return render(request,'formApp/insert.html',{'form':emptyForm})

@checkGroup
@login_required(login_url='employeeloginurl')
def empmodelinsert(request):
    emptyForm = EmpmodelForm()
    if request.method=='POST':
        dataForm = EmpmodelForm(request.POST,request.FILES)
        if dataForm.is_valid()==True:
            dataForm.save()
            messages.success(request,'Data is successfully')
            return render(request,'formApp/modelinsert.html',{'form':emptyForm})
        else:
            messages.error(request,'There is an error')
            return render(request,'formApp/modelinsert.html',{'form':dataForm})
    return render(request,'formApp/modelinsert.html',{'form':emptyForm})

def selectemployee(request,pno):
    emps = Employee.objects.all()
    pObj = Paginator(emps,2)
    emps = pObj.get_page(pno)
    print(pno)
    return render(request,'formApp/select.html',{'employees':emps})

def detailedpage(request,eno):
    emp = Employee.objects.get(empno=eno)
    return render(request,'formApp/detail.html',{'employee':emp})

@login_required(login_url='employeeloginurl')
def homepage(request):
    print(request.myValue)
    return render(request,'formApp/home.html')

def loginpage(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        valid_user = authenticate(request,username=uname,password=pwd)
        if valid_user !=None:
            login(request,valid_user)
            return redirect('employeehomeurl')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('employeeloginurl')
    return render(request,'formApp/login.html')

def logoutpage(request):
    logout(request)
    return redirect('employeeloginurl')

def signuppage(request):
    emptyForm = RegisterForm()
    if request.method == 'POST':
        dataForm = RegisterForm(request.POST)
        if dataForm.is_valid() == True:
            dataForm.save()
            return redirect('employeeloginurl')
        else:
            return render(request,'formApp/signup.html',{'form':dataForm})
    return render(request,'formApp/signup.html',{'form':emptyForm})

