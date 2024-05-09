from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def dbprocess(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        user = request.POST.get('user')
        feedback = request.POST.get('feedback')
        rating = int(request.POST.get('rating'))

        book = Book(author=author, user=user, feedback=feedback, rating=rating)
        book.save()

        return render(request,'databaseApp/insert.html')
    
