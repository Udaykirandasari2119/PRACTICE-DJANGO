from django.urls import path
from . import views

urlpatterns = [
    path('select/',views.selectData,name='selectrevurl'), #http//:127.0.0.1.8000  revision.select        
    path('insert/',views.insertData,name='insertrevurl'),
    path('update/<int:eno>/',views.updateData,name='updaterevurl'),
    path('delete/<int:eno>/',views.deleteData,name='deleterevurl'),
]    