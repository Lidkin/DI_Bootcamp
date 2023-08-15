from .models import (Department,
                        Employee,
                        Task,
                        Project)
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'description']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['name', 'email', 'phone_number']
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['name', 'description', 'due_date', 'completed']
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ['name', 'description', 'start_date', 'end_date']
        fields = '__all__'
