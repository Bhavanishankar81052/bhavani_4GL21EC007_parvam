from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10,unique=True)
    email = models.CharField(max_length=50)
    qualification = models.IntegerField()
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
