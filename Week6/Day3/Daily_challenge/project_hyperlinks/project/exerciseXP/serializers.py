from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='department-detail')
        
    class Meta:
        model = Department        
        fields = ('id', 'name', 'description', 'url')
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')

    class Meta:
        model = Employee
        fields = ('id', 'department', 'name', 'email', 'phone_number','url')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')

    class Meta:
        model = Task
        fields = ('id', 'description', 'due_date', 'completed', 'name', 'project','url')
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url =serializers.HyperlinkedIdentityField(view_name='project-detail')

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'employees','url')
        
