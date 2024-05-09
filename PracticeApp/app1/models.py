from django.db import models

# Create your models here.
class LibraryTable(models.Model):
    BookName=models.CharField(max_length=30)
    AuthorName=models.CharField(max_length=30)
    Price=models.IntegerField()
    FeedBack=models.CharField(max_length=40)
    Rating=models.IntegerField()
  
    def __str__(self):
        return self.BookName