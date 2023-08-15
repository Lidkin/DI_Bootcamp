from django.shortcuts import render
from rest_framework.response import Response
from .permissions import (IsDepartmentAdmin, )
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import (Department,
                     Employee,
                     Task,
                     Project)
from .serializers import (DepartmentSerializer,
                         EmployeeSerializer, 
                         TaskSerializer, 
                         ProjectSerializer)


class DepartmentListAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsDepartmentAdmin, IsAuthenticated, )

class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsDepartmentAdmin, )

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = DepartmentSerializer(queryset)
        return Response(serializer.data)  
  
class EmployeeListAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsDepartmentAdmin, IsAuthenticated,)

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    permission_classes = (IsDepartmentAdmin, IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = EmployeeSerializer(queryset)
        return Response(serializer.data)  

class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsDepartmentAdmin, IsAuthenticated, )

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 
    permission_classes = (IsDepartmentAdmin, )

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = TaskSerializer(queryset)
        return Response(serializer.data)  

class ProjectListAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsDepartmentAdmin, IsAuthenticated, )

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer 
    permission_classes = (IsDepartmentAdmin, )

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = ProjectSerializer(queryset)
        return Response(serializer.data)                  