from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Customer  
        fields = ['pk', 'first_name', 'last_name', 'email', 'phone_number', 'address']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Vehicle 
        fields = ['pk', 'vehicle_type','date_created','real_cost','size']


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:   
        model = VehicleType
        fields = ['pk', 'name']


class VehicleSizeSerializer(serializers.ModelSerializer):
    class Meta:   
        model = VehicleSize
        fields = ['pk', 'name']
          

class RentalSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Rental
        fields = ['pk', 'rental_date', 'return_date', 'customer', 'vehicle']

        
class RateSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Rate  
        fields = ['pk', 'daily_rate', 'vehicle_type', 'vehicle_size']




class RentalStationSerializer(serializers.ModelSerializer):
    class Meta:   
        model = RentalStation
        fields = ['pk', 'name', 'capacity', 'address_station']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Address  
        fields = ['pk', 'address', 'address2', 'city', 'country', 'postal_code']



class VehicleAtRentalStationSerializer(serializers.ModelSerializer):
    class Meta:   
        model = VehicleAtRentalStation
        fields = ['pk', 'arrival_date', 'departure_date', 'vehicle', 'rental-station']




