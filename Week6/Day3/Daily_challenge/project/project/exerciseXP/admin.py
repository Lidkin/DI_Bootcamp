from django.contrib import admin

# Register your models here.
from .models import Department, Employee, Task, Project

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Project)