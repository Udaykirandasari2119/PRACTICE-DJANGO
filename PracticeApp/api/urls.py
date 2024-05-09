from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('getEmployees',views.GetData,basename='employee')

urlpatterns = [
    path('getData/',views.getemployeedata),
    path('getDataEndPoint/',views.getEmpDataApi),
    path('modify/<int:pk>',views.handlemodifications),
    path('signup/',views.registeruser),
    path('login/',obtain_auth_token),
    path('getcbv/',views.GetListView.as_view()),
    
]

urlpatterns+=router.urls