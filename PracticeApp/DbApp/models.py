from django.db import models
from django.db.models.signals import pre_save
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
class Department(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=20)

    def __str__(self):
        return self.deptname

class Employee(models.Model):
    empno = models.IntegerField(primary_key = True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()
    department = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.empname

class Base(models.Model):
    empno = models.IntegerField()
    empname = models.CharField(max_length=20)
    
    class Meta:
         abstract = True

class Base1(Base):
        pass

class Base2(Base):
    address = models.CharField(max_length=50)

class Base3(Base):
     phno = models.CharField(max_length=13)

class Base4(Base):
     region = models.CharField(max_length=20) 

class DupEmployee(Employee):
     class Meta:
          proxy = True
          ordering = ['salary']       

class Base5(models.Model):
     empno = models.IntegerField(primary_key = True)

class Base6(Base5):
     empname = models.CharField(max_length=20)

class Car(models.Model):
     regno = models.IntegerField(primary_key=True)
     carModel = models.CharField(max_length=20)

class Driver(models.Model):
     licenseno = models.IntegerField(primary_key=True)
     name = models.CharField(max_length=20)
     cars = models.ManyToManyField(Car)    

def empinserthandler(sender,instance,*args,**kwargs):
     subject = 'Test email'
     message = '''
     Hi Team,
     Below details are newly inserted into employee
     {}-{}-{}
     Regards,
     Vcube team
     '''.format(instance.empname,instance.salary,instance.empno)
     send_mail(subject=subject,from_email=settings.EMAIL_HOST_USER,recipient_list=['udaykirandasari245@gmail.com'],message=message)

pre_save.connect(empinserthandler,sender=Employee)