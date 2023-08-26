from rest_framework import serializers
from .models import *

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  

class RentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalStation
        fields = '__all__'
        include = 'vehicle_at_station_vehicle'

class RentalRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalRate
        fields = '__all__'  

class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type_name = serializers.CharField(source='vehicle_type.name', read_only=True)
    last_rental = serializers.SerializerMethodField(read_only=True)
    current_station = serializers.SerializerMethodField(read_only=True)
    customer = serializers.HyperlinkedRelatedField(
        view_name='customers-detail',
        queryset=Customer.objects.all()
    )
    

    class Meta:
        model = Vehicle
        fields = '__all__'
        extra_fields = ['vehicle_type_name', 'last_rental', 'current_station', 'customer']
        
    def get_last_rental(self, obj):
        last_rental = Rental.objects.filter(vehicle_at_station__vehicle=obj).order_by('-rental_date').first()
        if last_rental:
            return {
                "rental_date": last_rental.rental_date,
                "return_date": last_rental.return_date,
                "customer": last_rental.customer,
                "station": last_rental.vehicle_at_station.rental_station.name
            }
        return None
    

    def get_current_station(self, obj):
        current_station = VehicleAtRentalStation.objects.filter(vehicle=obj).first()
        if current_station:
            return {
                "station": current_station.rental_station.name
            }
        return None

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'  

class VehicleSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSize
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'  

class VehicleAtRentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAtRentalStation
        fields = '__all__'   

                     