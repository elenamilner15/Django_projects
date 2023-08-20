from django.urls import path
from . import views

urlpatterns = [
    path('rentals/', views.RentalAPIView.as_view(), name='rental-list'),
    path('rentals/<int:pk>/', views.UpdateRentalAPIView.as_view(), name='rental-detail'),
    path('customers/', views.CustomerAPIView.as_view(), name='customer-list'),
    path('vehicles/', views.VehicleAPIView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', views.UpdateVehicleAPIView.as_view(), name='vehicle-detail'),
    path('rental-stations/', views.RentalStationAPIView.as_view(), name='rental-station-list'),
    path('rental-stations/<int:pk>/', views.UpdateRentalStationAPIView.as_view(), name='rental-station-detail'),
    path('rental-station-distribution/', views.RentalStationDistributionAPIView.as_view(), name='rental-station-distribution'),
    path('rental-station-distribute/', views.RentalStationDistributeAPIView.as_view(), name='rental-station-distribute'),
    path('rent/stats/monthly/', views.MonthlyRentalStats.as_view(), name='monthly-rental-stats'),
    path('rent/stats/popular_station/', views.PopularRentalStation.as_view(), name='popular-rental-station'),
    path('rent/stats/popular_vehicle_type/', views.PopularVehicleType.as_view(), name='popular-vehicle-type'),
]
