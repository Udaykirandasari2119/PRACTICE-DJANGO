"""
URL configuration for PracticeApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import debug_toolbar 
from django.conf.urls.static import static
from django.conf import settings
from app1 import views

urlpatterns = [
    path('__debug__/',include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('hello/',include('hello.urls')),
    path('second/',include('secondapp.urls')),
    path('dtl/',include('DTLApp.urls')),
    path('cal/',include('caluclator.urls')),
    path('templates/',include('templateApp.urls')),
    path('db/',include('DbApp.urls')),
    path('ca/',include('case.urls')),
    path('Revision/',include('RevisionApp.urls')),
    path('form/',include('formApp.urls')),
    path('stu/',include('students.urls')),
    path('session/',include('sessionApp.urls')),
    path('cache/',include('cacheApp.urls')),
    path('api/',include('api.urls')),
    path('sec/',include('second.urls')),
    path('dt/',include('dtl.urls')),
    path('clc/',include('calu.urls')),
    path('tem/',include('temp.urls')),
    path('app1/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('register/', views.RegisterPage, name='register'),
    path('suggest/',views.UserPage,name='suggest'),
    path('user/',views.UserDetailsPage,name='user'),
    path('available/',views.AvailablePage,name='available'),
    path('select/',views.selectfunction, name='select'),
    path('adminsecond/',views.AdminSecond,name='adminsecond'),
    path('delete/<int:pk>/',views.DeleteFunction,name='delete'),
    path('update/<int:pk>/',views.UpdateFunction,name='update'),
    path('userhome/',views.UserHome,name='userhome'),
    path('edit/',views.EditFunction,name='edit'),
    path('usersuggest/',views.SuggestPage,name='usersuggest'),
    path('useravailable/',views.UserAvailablePage,name='useravailable'),
    path('usermybooks/',views.UserMyBooks,name='usermybooks'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)