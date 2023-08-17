from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length = 50)
    course = models.ManyToManyField('Course')
    

class Course(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)