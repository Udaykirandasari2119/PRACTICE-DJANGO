from django.shortcuts import render
from django.urls import reverse
from DbApp.models import Employee
from django.views.decorators.cache import cache_page
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@cache_page(60)
def cachehandling(request):
    emps = Employee.objects.all()

    return render(request,'cacheApp/cache.html',{'employee':emps})

class Firstview(View):
    def get(self,request):
        return render(request,'cacheApp/class.html')
    
    def post(self,request):
        txt = request.POST['t1']
        return render(request,'cacheApp/class.html',{'txt':txt})
    
def firstview(request):
    if request.method == 'POST':
        res = request.POST['t1']
        return render(request,'cacheApp/class.html',{'txt':res})
    
    return render(request,'cacheApp/class.html')

class SecondView(Firstview):
    def get(self,request):
        return HttpResponse('SecondView get response')
    
class SelectView(LoginRequiredMixin,ListView):
    login_url = 'employeeloginurl'
    model = Employee
    template_name = 'cacheApp/employee_select.html'
    

class InsertView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'cacheApp/emp_insert.html'

    def get_success_url(self):
        return reverse('cbvselecturl')

class EmpDetail(DetailView):
    model = Employee
    template_name = 'cacheApp/employee_detail.html'

class EmpUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'cacheApp/employee_update.html'

    def get_success_url(self):
        return reverse('cbvselecturl')
    
class EmpDelte(DeleteView):
    model = Employee

    template_name = 'cacheApp/employee_delete.html'

    def get_success_url(self):
        return reverse('cbvselecturl')
