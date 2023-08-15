from django.shortcuts import render
from .permissions import IsDepartmentAdmin
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                     HTTP_201_CREATED, 
                                     HTTP_400_BAD_REQUEST, 
                                     HTTP_204_NO_CONTENT)
from .models import (Department,
                     Employee,
                     Task,
                     Project)
from .serializers import (DepartmentSerializer,
                         EmployeeSerializer, 
                         TaskSerializer, 
                         ProjectSerializer)
# Create your views here.


class DepartmentAPIView(APIView):
    permission_classes = IsDepartmentAdmin
    
    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) 

    def put(self, request, id, *args, **kwargs):
        department = Department.objects.get(id=id)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        department = Department.objects.get(id=id)
        if department.is_valid():
            department.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(message='no such a department', status=HTTP_400_BAD_REQUEST)

class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) 

    def put(self, request, id, *args, **kwargs):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        employee = Employee.objects.get(id=id)
        if employee.is_valid():
            employee.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(message='no such a employee', status=HTTP_400_BAD_REQUEST)

class TaskAPIView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) 

    def put(self, request, id, *args, **kwargs):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        task = Task.objects.get(id=id)
        if task.is_valid():
            task.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(message='no such a task', status=HTTP_400_BAD_REQUEST)

class ProjectAPIView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    

    def put(self, request, pk, *args, **kwargs):
        project = Progect.objects.get(id=id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        project = Project.objects.get(id=id)
        if project.is_valid():
            project.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(message='no such a project', status=HTTP_400_BAD_REQUEST)     


# class DepartmentAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Department.objects.all()
    # serializer_class=DepartmentSerializer
# 
# class EmployeeAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Department.objects.all()
    # serializer_class = DepartmentSerializer    