from .models import Hotel, Room
from rest_framework import viewsets, permissions
from .serializers import HotelSerializer


# Hotel Viewset
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HotelSerializer
