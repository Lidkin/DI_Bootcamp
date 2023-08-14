from django.urls import path
from .views import StudentView, StudentDetail

urlpatterns = [
    path('students/', StudentView.as_view(), name='student_list'),
    path('student/<int:pk>', StudentDetail.as_view(), name='student-detail')
]