from django.db import models

# Create your models here.

class Book(models.Model):
    auther = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=50)
    

    def __str__(self):
        return self.auther