import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import *
from faker import Faker

fake = Faker()
tav =21 #total amount of vehicles in company

def create_const():
    # vehicle types
    vehicle_type_choices = ['bike', 'scooter']
    for vehicle_type_str in vehicle_type_choices:
        VehicleType.objects.get_or_create(name=vehicle_type_str)
    
    # vehicle sizes
    vehicle_size_choices = ['S', 'M', 'L']
    for vehicle_size_str in vehicle_size_choices:
        VehicleSize.objects.get_or_create(name=vehicle_size_str)
        
    vehicle_type_choices = ['bike', 'scooter']
    vehicle_size_choices = ['S', 'M', 'L']
    for vehicle_type_str in vehicle_type_choices:
            vehicle_type_instance, _ = VehicleType.objects.get_or_create(name=vehicle_type_str)
            for vehicle_size_str in vehicle_size_choices:
                vehicle_size_instance, _ = VehicleSize.objects.get_or_create(name=vehicle_size_str)
                
                rate = Rate.objects.create(
                    daily_rate=fake.pydecimal(min_value=100, max_value=800, right_digits=2),
                    vehicle_type=vehicle_type_instance,
                    vehicle_size=vehicle_size_instance
                )
                rate.save()
    print(f"CREATED Data Entries")            
create_const() 
