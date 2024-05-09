from django.urls import path
from . import views

urlpatterns = [
    path('',views.cachehandling),
    path('class/',views.SecondView.as_view()),
    path('functionview/',views.firstview,name='functionviewurl'),
    path('select/',views.SelectView.as_view(),name='cbvselecturl'),
    path('insert/',views.InsertView.as_view()),
    path('detail/<int:pk>',views.EmpDetail.as_view()),
    path('update/<int:pk>',views.EmpUpdate.as_view()),
    path('delete/<int:pk>',views.EmpDelte.as_view()),
]
