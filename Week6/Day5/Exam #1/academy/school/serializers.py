from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.BaseSerializes):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.BaseSerializes):
    class Meta:
        model = Course
        fields = '__all__'