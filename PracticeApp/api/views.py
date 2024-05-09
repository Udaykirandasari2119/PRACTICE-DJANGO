from django.shortcuts import render,get_object_or_404
from DbApp.models import Employee
from django.http import JsonResponse
import json
from .serializer import EmpSerializers,UserSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_200_OK
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework .viewsets import ViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView


# Another module where you're trying to import EmpSerializer



# Create your views here.
def getemployeedata(request):
    emps=Employee.objects.all().values()
    data=[ d for d in emps]
    # print(data)
    output=json.dumps(data)
    
    return JsonResponse(output,safe=False)
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def getEmpDataApi(request):
    if request.method=='GET':
        emps=Employee.objects.all() 

        employee=EmpSerializers(emps,many=True)
        return Response(employee.data)
    elif request.method=='POST':
       emps= EmpSerializers(data=request.data)# data is ana attribute 
       if emps.is_valid()==True:
           emps.save()
           return Response(status=HTTP_201_CREATED)
       else:
           return Response(data=emps.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])  #api_view its used to  handle to accept which methods will accept 
def handlemodifications(request,pk):
    empObj=Employee.objects.get(empno=pk)
    if request.method=='GET':
        emp=EmpSerializers(empObj)
        return Response(emp.data,status=HTTP_200_OK)
        
    elif request.method=='PUT':
        emp=EmpSerializers(empObj,data=request.data)
        if emp.is_valid()==True:
            emp.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        empObj.delete()
        return Response(status=HTTP_200_OK)
    
@api_view(['POST'])
def registeruser(request):
    user= UserSerializers(data=request.data)
    if user.is_valid()==True:
        udetails =user.save() #its is returing an objects
        tkn= Token.objects.create(user=udetails)
        userDetails={
            'username':udetails.username,
            'token':tkn.key,
        }
        return Response(userDetails, status=HTTP_201_CREATED)
    else:
        return Response(user.errors,status=HTTP_400_BAD_REQUEST)
    
class GetListView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    #pagination_class = PageNumberPagination

class GetData(ViewSet):
    def list(self,request):  #list is for get request
        emps = Employee.objects.all()
        #data = get_object_or_404(emps,pk=pk)

        empData = EmpSerializers(emps,many=True)
        return Response(empData.data,status=HTTP_200_OK)
    
    def retrieve(self,request,pk=None):
        emps = Employee.objects.all()  #it is a fetch request
        employee = get_object_or_404(emps,pk=pk)
        empSer = EmpSerializers(employee)
        return Response(empSer.data,status=HTTP_200_OK)
    
    def create(self,request):
        employee = EmpSerializers(data=request.data)

        if employee.is_valid()==True:
            employee.save()
        return Response(status=HTTP_201_CREATED)