from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import students

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                student = students.objects.get(username=username, password=password)
                # Redirect to student dashboard or any other page upon successful login
                return redirect('dashboard')
            except students.DoesNotExist:
                # If user doesn't exist or password is incorrect, display error
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
