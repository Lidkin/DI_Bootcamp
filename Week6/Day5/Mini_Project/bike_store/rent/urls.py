from django.urls import path
from .views import *

urlpatterns = [
    path('rental', RentalList.as_view(), name='rental-list'),
    path('rental/<int:pk>', RentalDetail.as_view(), name='rental-detail'),
    path('station', StationsList.as_view(), name='stations-list'),
    path('station/add', StationAdd.as_view(), name='station-add'),
    path('station/<int:pk>', StationDetail.as_view(), name='station-detail'),
    path('station/distribution', StationDistribution.as_view(), name='distribution'),
    path('station/distribute', DistributeVehicle.as_view(), name='distribute'),
    path('customer/', CustomerList.as_view(), name='customers-list'),
    path('customer/<int:pk>', CustomerDetail.as_view(), name='customers-detail'),
    path('customer/add', CustomerAdd.as_view(), name='customer-add'),
    path('vehicle', VehicleList.as_view(), name='vehicle-list'),
    path('vehicle/<int:pk>', VehicleDetail.as_view(), name='vehicle-detail'),
    path('vehicle/add', VehicleAdd.as_view(), name='vehicle-add'),
]
