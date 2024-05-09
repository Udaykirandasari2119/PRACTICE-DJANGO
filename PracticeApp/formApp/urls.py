from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginpage,name='employeeloginurl'),
    path('logout',views.logoutpage,name='employeelogouturl'),
    path('signupurl',views.signuppage,name='employeesignupurl'),
    path('home',views.homepage,name='employeehomeurl'),
    path('First/',views.firstForm),
    path('insert/',views.empinsert),
    path('modelinsert/',views.empmodelinsert,name='employeeinserturl'),
    path('select/<int:pno>',views.selectemployee,name='employeeselecturl'),
    path('detail/<int:eno>',views.detailedpage,name='employeedetailurl'),
]