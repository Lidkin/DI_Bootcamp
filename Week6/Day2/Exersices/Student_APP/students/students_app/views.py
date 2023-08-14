from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

# Create your views here.

class StudentView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)      


class StudentDetail(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk, *args, **kwargs):
        try:
            article = Student.objects.get(pk=pk)    
            serializer = StudentSerializer(article)
            return Response(serializer.data, status=HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        article = Student.objects.get(pk=pk)
        serializer = StudentSerializer(article, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            article = Student.objects.get(pk=pk)
            article.delete()   
            return Response(status=HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:        
            return Response(status=HTTP_404_NOT_FOUND)   