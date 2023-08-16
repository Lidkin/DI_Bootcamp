from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('departments', viewset = DepartmentViewSet)
router.register('employees', viewset = EmployeeViewSet)
router.register('tasks', viewset = TaskViewSet)
router.register('projects', viewset = ProjectViewSet)

department_detail = DepartmentViewSet.as_view({
       'get': 'list',
       'post': 'create',
       'put': 'update',
       'delete': 'destroy'
    })

employee_detail = EmployeeViewSet.as_view({
       'get': 'list',
       'post': 'create',
       'put': 'update',
       'delete': 'destroy'
    })

task_detail = TaskViewSet.as_view({
       'get': 'list',
       'post': 'create',
       'put': 'update',
       'delete': 'destroy'
    })

project_detail = ProjectViewSet.as_view({
       'get': 'list',
       'post': 'create',
       'put': 'update',
       'delete': 'destroy'
    })    

urlpatterns = [
   path('', include(router.urls)),
   path('department/', department_detail, name='department-detail'),
   path('employee/', employee_detail, name='employee-detail'),
   path('task/', task_detail, name='task-detail'),
   path('project/', project_detail, name='project-detail'),

]