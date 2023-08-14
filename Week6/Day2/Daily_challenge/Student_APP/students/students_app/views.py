from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

# Create your views here.

class StudentMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = StudentSerializer

   # add method for filtered queryset
    def get_queryset(self):
        queryset = Student.objects.all()
        date_joined = self.request.query_params.get('date_joined')
        if date_joined:
            queryset = queryset.filter(date_joined=date_joined)
        return queryset

    # regular methods
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    

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