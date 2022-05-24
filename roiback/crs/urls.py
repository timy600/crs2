"""roiback URL Configuration
"""
from django.urls import include, path

urlpatterns = [
    path('availability/', include('crs.apis.availability.urls')),
    path('hotels/', include('crs.apis.hotels.urls')),
    path('rooms/', include('crs.apis.rooms.urls')),
    path('rates/', include('crs.apis.rates.urls')),
    path('inventories/', include('crs.apis.inventories.urls')),
]
