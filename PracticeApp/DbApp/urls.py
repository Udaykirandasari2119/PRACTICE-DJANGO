from django.urls import path
from . import views

urlpatterns = [
    path('',views.dbprocessing,name='inserturl'),
    path('select/',views.selectEmployee,name='selecturl'),
    path('update/<int:eno>/',views.detailEmployee,name='updateurl'),
    path('delete/<int:eno>/',views.deleteEmployee,name='deleteurl'),
]