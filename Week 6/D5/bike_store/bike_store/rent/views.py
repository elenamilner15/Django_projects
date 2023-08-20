from datetime import date
from django.shortcuts import render, get_object_or_404

from django.http import Http404, JsonResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

#________________________________________________________________
class RentalAPIView(APIView):
    def get (self, request):
        queryset=Rental.objects.filter(return_date__isnull=True).order_by('rental_date')       
        serializer = RentalSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
       
#________________________________________________________________
   
class UpdateRentalAPIView(APIView):    
    def get_object(self, pk):
        try:
            print(pk)
            return Rental.objects.get(pk=pk)
            
        except Rental.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        print(obj)
        serializer = RentalSerializer(obj)
        return Response(serializer.data)
  
    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = RentalSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'deleted successfully'}, status=204)

#________________________________________________________________

class CustomerAPIView(APIView):
    def get (self, request):
        queryset=Customer.objects.all()        
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
    
#________________________________________________________________
class VehicleAPIView(APIView):
    def get (self, request):
        queryset=Customer.objects.values('vehicle_type').annotate(count=models.Count('id'))        
        serializer = VehicleSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
    
#________________________________________________________________   
class UpdateVehicleAPIView(APIView):    
    def get_object(self, pk):
        try:
            print(pk)
            return Vehicle.objects.get(pk=pk)
            
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        print(obj)
        serializer = VehicleSerializer(obj)
        return Response(serializer.data)
  
    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = VehicleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'deleted successfully'}, status=204)

#________________________________________________________________

class RentalStationAPIView(APIView):
    def get (self, request):
        queryset=RentalStation.objects.all()        
        serializer = RentalStationSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
#________________________________________________________________   
class UpdateRentalStationAPIView(APIView):    
    def get_object(self, pk):
        try:
            print(pk)
            return RentalStation.objects.get(pk=pk)
            
        except RentalStation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        print(obj)
        serializer = RentalStationSerializer(obj)
        return Response(serializer.data)
  
#___________________________________________________________________


class RentalStationDistributionAPIView(APIView):
    def get(self, request):
        distribution_stats = []

        rental_stations = RentalStation.objects.all()
        for station in rental_stations:
            vehicle_at_rental_stations = VehicleAtRentalStation.objects.filter(
                arrival_date__isnull=True,
                rental_station=station
            )
            vehicles_count = vehicle_at_rental_stations.count()

            distribution_stats.append({
                "station_name": station.name,
                "vehicles_count": vehicles_count
            })

        return Response(distribution_stats)
#____________________________________________________________________________

class RentalStationDistributeAPIView(APIView):
    def post(self, request):
        try:
            # Get all rental stations and their capacities
            rental_stations = RentalStation.objects.all().order_by('capacity')
            total_capacity = sum(station.capacity for station in rental_stations)
            
            # Get all available vehicles for distribution
            available_vehicles = Vehicle.objects.filter(vehicleatrentalstation__arrival_date__isnull=False)
            
            # Distribute vehicles evenly based on % of capacity
            for station in rental_stations:
                vehicles_to_assign = int((station.capacity / total_capacity) * available_vehicles.count())
                print(vehicles_to_assign)
                for _ in range(vehicles_to_assign):
                    if available_vehicles:
                        vehicle = available_vehicles.first()
                        print(vehicle)
                        VehicleAtRentalStation.objects.create(
                            arrival_date=date.today(),
                            vehicle=vehicle,
                            rental_station=station
                        )
                        available_vehicles = available_vehicles.exclude(pk=vehicle.pk)
            
            return Response({"message": "Vehicles distributed successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

#_______________________________________________________________________________
#Daily Challenge
from django.db.models import Count
from django.db.models.functions import TruncMonth

class MonthlyRentalStats(APIView):
    def get(self, request):
        stats = Rental.objects.annotate(month=TruncMonth('rental_date')) \
            .values('month') \
            .annotate(rental_count=Count('id')) \
            .order_by('month')
        
        result = {stat['month'].strftime('%Y-%m'): stat['rental_count'] for stat in stats}
        
        return JsonResponse(result)
    
#_______________________________________________________________________________
class PopularRentalStation(APIView):
    def get(self, request):
        stats = Rental.objects.values('vehicle__vehicleatrentalstation__rental_station__name') \
            .annotate(rental_count=Count('id')) \
            .order_by('-rental_count')
        
        result = {stat['vehicle__vehicleatrentalstation__rental_station__name']: stat['rental_count'] for stat in stats}
        
        return JsonResponse(result)
    
#______________________________________________________________________________  
class PopularVehicleType(APIView):
    def get(self, request):
        stats = Rental.objects.values('vehicle__vehicle_type__name') \
            .annotate(rental_count=Count('id')) \
            .order_by('-rental_count')
        
        result = {stat['vehicle__vehicle_type__name']: stat['rental_count'] for stat in stats}
        
        return JsonResponse(result)