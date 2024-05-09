from django.urls import path
from .import views
from.models import Book

urlpatterns = [
    path('',views.dbprocess),
]