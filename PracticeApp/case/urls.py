from django.urls import path
from . import views

urlpatterns = [
    path('',views.countwords,name='countwords'),
]