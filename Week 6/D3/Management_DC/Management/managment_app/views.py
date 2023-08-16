
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from .models import *
from .views import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import permissions
from .permissions import IsDepartmentAdmin
#________________________________________________________________

class DepartmentAPIView(APIView):
    permission_classes = [IsDepartmentAdmin]
    def get (self, request):
        queryset=Department.objects.all()        
        serializer = DepartmentSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
    
#________________________________________________________________
   
class UpdateDepartmentAPIView(APIView): 
    permission_classes = [IsDepartmentAdmin]  
    def get_object(self, pk):
        try:
            print(pk)
            return Department.objects.get(pk=pk)
            
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        print(obj)
        serializer = DepartmentSerializer(obj, context={'request': request})
        return Response(serializer.data)
  
    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = DepartmentSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'deleted successfully'}, status=204)

#________________________________________________________________

class EmployeeAPIView(APIView):
    permission_classes = [IsDepartmentAdmin]
    def get (self, request):
        queryset=Employee.objects.all()        
        serializer = EmployeeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
#________________________________________________________________

class UpdateEmployeeAPIView(APIView):   
    permission_classes = [IsDepartmentAdmin]
    def get_object(self, pk):
        try:
            print(pk)
            return Employee.objects.get(pk=pk)
            
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        print(obj)
        serializer = EmployeeSerializer(obj, context={'request': request})
        return Response(serializer.data)
  
    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = EmployeeSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'deleted successfully'}, status=204)

#________________________________________________________________

class ProjectAPIView(APIView):
    permission_classes = [IsDepartmentAdmin]
    def get (self, request):
        queryset=Project.objects.all()        
        serializer = ProjectSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
#________________________________________________________________     
  
class UpdateProjectAPIView(APIView):  
    permission_classes = [IsDepartmentAdmin]
    def get_object(self, pk):
        try:
            print(pk)
            return Project.objects.get(pk=pk)
            
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        print(obj)
        serializer = ProjectSerializer(obj, context={'request': request})
        return Response(serializer.data)
  
    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = ProjectSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'deleted successfully'}, status=204)

#________________________________________________________________
class TaskAPIView(APIView):
    permission_classes = [IsDepartmentAdmin]
    def get (self, request):
        queryset=Task.objects.all()        
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
#________________________________________________________________    
     
class UpdateTaskAPIView(APIView):    
    permission_classes = [IsDepartmentAdmin]
    def get_object(self, pk):
        try:
            print(pk)
            return Task.objects.get(pk=pk)
            
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        print(obj)
        serializer = TaskSerializer(obj, context={'request': request})
        return Response(serializer.data)
  
    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = TaskSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'deleted successfully'}, status=204)

#________________________________________________________________



