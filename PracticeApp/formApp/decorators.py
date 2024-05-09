from django.shortcuts import redirect
def checkSuperUser(fun):
    def innerFun(request):
        if request.user.is_superuser == True:
            return fun(request)
        else:
            return redirect('employeehomeurl')
    return innerFun

from django.shortcuts import redirect

def checkGroup(fun):
    def innerFun(request):
        # Checking if the user is authenticated and belongs to any group
        if request.user.is_authenticated and request.user.groups.exists():
            # Fetching the first group object and checking if 'python' is in its name
            if 'Python' in str(request.user.groups.all()[0]):
                return fun(request)
        # Redirecting to the employee home URL if the user is not authenticated or doesn't belong to any group with 'python' in its name
        return redirect('employeehomeurl')
    return innerFun
