from django.urls import path
from .import views

urlpatterns=[
    path('fir/',views.firstfunction),
    path('sec/',views.secfunction)
]