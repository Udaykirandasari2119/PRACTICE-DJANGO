from rest_framework.serializers import ModelSerializer
from DbApp.models import Employee
from django.contrib.auth.models import User

class EmpSerializers(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['empno','empname','salary','department']

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']