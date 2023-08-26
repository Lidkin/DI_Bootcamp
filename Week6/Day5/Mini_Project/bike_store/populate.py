import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import *
from faker import Faker

fake = Faker()

def create_customers(number):
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

    print(f"CREATED {number} Customers")

def create_rent_stations(number):
    for _ in range(number):
        rental = RentalStation(
            name=fake.street_address(),
            capacity=fake.random_int(min=10, max=500),
            address=Address.objects.get(id=fake.unique.random_int(min=1, max=100))
        )
        rental.save()

def create_vehicle(number):
    for _ in range(number):
        vehicle_type = VehicleType(
            name=fake.unique.word()
        ) 
        vehicle_type.save() 

        vehicle_size = VehicleSize(
            name=fake.unique.text()[0:50]
        )
        vehicle_size.save()

        vehicle = Vehicle(
            vehicle_type=vehicle_type,
            date_created=fake.date(),
            real_cost=fake.random_digit(),
            size=vehicle_size
        )
        vehicle.save()

# create_customers(100)
# create_rent_stations(10)
# create_vehicle(5)