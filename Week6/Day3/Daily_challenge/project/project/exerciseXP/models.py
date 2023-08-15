from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    # admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)

class Employee(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE) 

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    employees = models.ManyToManyField('Employee')