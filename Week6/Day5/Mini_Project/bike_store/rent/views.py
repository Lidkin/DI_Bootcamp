from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist, BadRequest
from django.db.models import Count
from django.forms.models import model_to_dict
import json, random

class RentalDetail(APIView):

    def get(self, request, pk, *args, **kwargs):
        try:
            item = Rental.objects.get(pk=pk)
            serializer = RentalSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:    
            return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)    

    def put(self, request, pk, *args, **kwargs):
        try:
            item = Rental.objects.get(pk=pk)
            serializer = RentalSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK) 
            else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
        except ObjectDoesNotExist as e:    
            return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)     

    def delete(self, request, pk, *args, **kwargs):
        try:
            item = Rental.objects.get(pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)     
        except ObjectDoesNotExist as e:    
            return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)   

class RentalList(APIView):

    def get(self, request, *args, **kwargs):
        rentals = Rental.objects.order_by('return_date')
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StationsList(APIView):

    def get(self, request, *args, **kwargs):
        stations = RentalStation.objects.all()
        serializer = RentalStationSerializer(stations, many=True) 
        return Response(data=serializer.data)       


class StationAdd(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class StationDetail(APIView):
    def get(self, request, pk:int, *args, **kwargs):
        try:
            station = RentalStation.objects.get(id=pk)
            data_station = RentalStationSerializer(station).data
            try:
                station_vehicle = VehicleAtRentalStation.objects.filter(rental_station_id=pk).select_related('vehicle')
                vehicles = []
                for s_v in station_vehicle: 
                    #vehicle = Vehicle.objects.create(size=s_v.vehicle.size.name, vehicle_type=s_v.vehicle.vehicle_type.name) # didn't work :(
                    vehicle = {
                        "vehicle_id": s_v.vehicle.id,
                        "vehicle_size": s_v.vehicle.size.name,
                        "vehicle_type": s_v.vehicle.vehicle_type.name,
                        "arrival_date": s_v.arrival_date,
                        "departure_date": s_v.departure_date,
                    }
                    vehicles.append(vehicle)    
                data_station["vehicles"] = vehicles
            except:       
                data_station
            return Response(data_station, status=status.HTTP_200_OK)  
        except ObjectDoesNotExist as e:
            return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)                                               

class CustomerList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            customers = Customer.objects.all().order_by('last_name', 'first_name')
            serializer = CustomerSerializer(customers, many=True).data
            return Response(serializer, status=status.HTTP_200_OK)    
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    def get(self, request, pk:int, *args, **kwargs):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(instance=customer, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)

class CustomerAdd(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data) 
        if serializer.is_valid():  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)               

class VehicleList(APIView): 
    
    def get(self, request, *args, **kwargs):
        try:
            vehicles = Vehicle.objects.all().select_related('vehicle_type').order_by('vehicle_type__name')
            serializer = VehicleSerializer(instance=vehicles, context={'request': request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetail(APIView):
        
        def get(self, request, pk:int, *args, **kwargs):
            try:
                vehicle = Vehicle.objects.get(pk=pk)
                serializer = VehicleSerializer(instance=vehicle, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist as e:
                return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)     

        def put(self, request, pk:int, *args, **kwargs):
            try:
                vehicle = Vehicle.objects.get(pk=pk)
                serializer = VehicleSerializer(instance=vehicle, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            except ObjectDoesNotExist as e:
                return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)    

        def delete(self, request, pk:int, *args, **kwargs):
            try:
                vehicle = Vehicle.objects.get(pk=pk)
                vehicle.delete()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT) 
            except ObjectDoesNotExist as e:
                return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)    

class VehicleAdd(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VehicleSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

class StationDistribution(APIView):
    def get(self, request):
        distribution_stats = RentalStation.objects.annotate(vehicle_count=Count('vehicleatrentalstation')).values('name', 'vehicle_count')
        
        return Response({'distribution_stats': list(distribution_stats)})

class DistributeVehicle(APIView):
    def post(self, request):
        vehicle_ids = list(Vehicle.objects.values_list('id', flat=True))
        stations = RentalStation.objects.filter(vehicleatrentalstation=None)
        
        VehicleAtRentalStation.objects.all().delete()

        for station in stations:
            available_capacity = min(station.capacity, len(vehicle_ids))
            if available_capacity > 0:
                selected_vehicle_ids = random.sample(vehicle_ids, available_capacity)
                for vehicle_id in selected_vehicle_ids:
                    vehicle_at_station = VehicleAtRentalStation(vehicle_id=vehicle_id, rental_station=station)
                    vehicle_at_station.save()
                    vehicle_ids.remove(vehicle_id)

        
        distribution_stats = RentalStation.objects.annotate(vehicle_count=Count('vehicleatrentalstation')).values('name', 'vehicle_count')
        
        return Response({'message': 'Vehicles successfully distributed among stations.', 'distribution_stats': list(distribution_stats)}, status=status.HTTP_201_CREATED)
