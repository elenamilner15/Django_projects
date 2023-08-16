from django import views
from django.urls import path
from .views import *


urlpatterns = [
    path('departments/', DepartmentAPIView.as_view()),
    path('departments/<int:pk>/', UpdateDepartmentAPIView.as_view()),
    
    path('employees/', EmployeeAPIView.as_view()),
    path('employees/<int:pk>/', UpdateEmployeeAPIView.as_view()),
    
    path('projects/', ProjectAPIView.as_view(), name='Project-operations'),
    path('projects/<int:pk>/', UpdateProjectAPIView.as_view()),
    
    path('tasks/', TaskAPIView.as_view(), name='Task-operations'),
    path('tasks/<int:pk>/', UpdateTaskAPIView.as_view()),
]











