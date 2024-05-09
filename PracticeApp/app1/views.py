from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import LibraryTable


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('Your password and confirm password are not same')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            uname=request.POST.get('username')
            pass2=request.POST.get('password2')
            print(uname)
            print(pass2)
            if uname=="Sudhakarreddy" and pass1=="sudhakarreddy55" :
                return redirect('user')
            else:
                return redirect('userhome')

            
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def RegisterPage(request):
    if request.method == 'POST':
        book = (request.POST['book'])
        author = (request.POST['author'])
        price = int(request.POST['price'])
        feed = (request .POST['feed'])
        rating = int(request.POST['rating'])

        data = LibraryTable(BookName=book,AuthorName=author,Price=price,FeedBack=feed,Rating=rating)
        data.save()
        return redirect('select')
    else:
        return render(request,'register.html')

def selectfunction(request):
    data=LibraryTable.objects.all()
  
        
    return render(request,'select.html',{'data':data})

def DeleteFunction(requet,pk):
    emps=LibraryTable.objects.filter(id=pk)
    emps.delete()
    return redirect('select')
    
def UpdateFunction(request, pk):
    if request.method=='POST':
        no=int(request.POST['t1'])
        book=request.POST['t2']
        author=request.POST['t3']
        price=int(request.POST['t4'])
        feedback=request.POST['t5']
        rating=int(request.POST['t6'])
        emps=LibraryTable(id=no,BookName=book,AuthorName=author,Price=price,FeedBack=feedback,Rating=rating)
        emps.save()
        return redirect('select')

    emp=LibraryTable.objects.filter(id=pk)
    return render(request,'update.html',{'data':emp})

def UserPage(request):
    return render(request,'suggest.html')

def UserDetailsPage(request):
    return render(request,'user.html')

def AvailablePage(request):
    return render(request,'available.html')

def AdminSecond(request):
    return render(request,'adminsecond.html')

def UserHome(request):
    return render(request,'userhome.html')

def EditFunction(request):
    return render(request,'edit.html')

def SuggestPage(request):
    return render(request,'usersuggest.html')

def UserAvailablePage(request):
      data=LibraryTable.objects.all()
      return render(request,'useravailable.html',{'data':data})

def UserMyBooks(request):
    return render(request,'usermybooks.html')