import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import *
from faker import Faker

fake = Faker()
tav =21 #total amount of vehicles in company

def create_data(number): 
    vehicle_type_choices = ['bike', 'scooter']
    vehicle_size_choices = ['S', 'M', 'L']
    
    for _ in range(number):
        address = Address(
            address=fake.street_address(),
            address2=fake.secondary_address(),
            city=fake.city(),
            country=fake.country(),
            postal_code=fake.zipcode()
        )
        address.save()

        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=address
        )
        customer.save()
        
        
        vehicle_type_str = random.choice(vehicle_type_choices)
        vehicle_size_str = random.choice(vehicle_size_choices)

        vehicle_type_instance = VehicleType.objects.get(name=vehicle_type_str)
        vehicle_size_instance = VehicleSize.objects.get(name=vehicle_size_str)
        
        existing_vehicle_count = Vehicle.objects.count()
        date_created = fake.date_between(start_date='-10y', end_date='now') #Date when vehicle was build (??)      
        if existing_vehicle_count < tav:
            vehicle = Vehicle.objects.create(
                vehicle_type=vehicle_type_instance,
                date_created=date_created, 
                real_cost=fake.pydecimal(min_value=100, max_value=1000, right_digits=2),
                size=vehicle_size_instance
            )             
            vehicle.save()
        else:
            vehicle = random.choice(Vehicle.objects.all()) 
            vehicle.save()

        
        rental_date = fake.date_this_month()#moved here!!!!!!!!!!!!!!!!
        return_date = fake.date_between_dates(date_start=rental_date) if fake.boolean() else None  # Generate return date after rental_date or None
        
        
        rental = Rental.objects.create(
            rental_date=rental_date,
            return_date=return_date,
            customer=customer,            
            vehicle=vehicle
        )
        rental.save()  
        
        existing_station_count = RentalStation.objects.count()
        if existing_station_count < 6:
            address_station = AddressStation(
                address=fake.street_address(),
                city=fake.city(),
                country=fake.country(),
                postal_code=fake.zipcode()
            )
            address_station.save()

            rental_station = RentalStation.objects.create(
                name=fake.company(),
                capacity=fake.random_int(min=5, max=15),
                address=address_station
            )
            rental_station.save()    
    
        else:
            rental_station = random.choice(RentalStation.objects.all()) 
            
        existing_rental_count = Rental.objects.count()
        # print(existing_rental_count)        
       
        if existing_vehicle_count < tav:   
            vehicle_at_rental_station = VehicleAtRentalStation.objects.create(
                arrival_date=return_date,  # arrival date = return date
                departure_date=rental_date,  # departure date = rental date
                vehicle=vehicle,
                rental_station=rental_station
            )
            vehicle_at_rental_station.save()   
            
        else:
            # Modify existing vehicle_at_rental_station          
            vehicle_at_rental_stations = VehicleAtRentalStation.objects.filter(vehicle=vehicle)
            for vehicle_at_rental_station in vehicle_at_rental_stations:          
                arrival_date=return_date,  # arrival date = return date
                departure_date=rental_date,  # departure date = rental date
                vehicle=vehicle,
                rental_station=rental_station                
            vehicle_at_rental_station.save()   
            
                 
     
    print(f"CREATED {number} Data Entries")
    
create_data(10)