from django.urls import path
from .views import DepartmentDetailAPIView, DepartmentListAPIView, EmployeeListAPIView, EmployeeDetailAPIView

urlpatterns = [
    path('departments/list/<int:pk>', DepartmentDetailAPIView.as_view(), name='department-list-id'),
    path('departments/list', DepartmentListAPIView.as_view(), name='department-list'),
    path('employees/list/<int:pk>', EmployeeDetailAPIView.as_view(), name='department-list-id'),
    path('employees/list', EmployeeListAPIView.as_view(), name='department-list'),
    path('tasks/list/<int:pk>', DepartmentDetailAPIView.as_view(), name='department-list-id'),
    path('tasks/list', DepartmentListAPIView.as_view(), name='department-list'),
    path('projects/list/<int:pk>', DepartmentDetailAPIView.as_view(), name='department-list-id'),
    path('projects/list', DepartmentListAPIView.as_view(), name='department-list'),
]