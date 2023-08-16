from rest_framework import serializers
from .models import Department, Employee, Project, Task

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='department-detail')
    class Meta:   
        model = Department  
        fields = ['url', 'pk', 'name', 'description']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')
    class Meta:
        model = Employee
        fields = ['url', 'pk', 'name', 'email', 'phone_number', 'department', 'projects']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-detail')
    class Meta:
        model = Project
        fields = ['url', 'pk', 'name', 'description', 'start_date', 'end_date']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    class Meta:
        model = Task
        fields = ['url', 'pk', 'name', 'description', 'due_date', 'completed', 'project']
