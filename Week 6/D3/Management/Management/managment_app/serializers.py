from rest_framework import serializers
from .models import Department, Employee, Project, Task

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Department  
        fields = ['pk', 'name', 'description']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['pk', 'name', 'email', 'phone_number', 'department', 'projects']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['pk', 'name', 'description', 'start_date', 'end_date']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['pk', 'name', 'description', 'due_date', 'completed', 'project']
