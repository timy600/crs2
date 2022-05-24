from rest_framework import serializers
from crs.models import Hotel, Room, Rate, Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["availability", "date"]


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ["code", "name", "price", "inventories"]
        depth = 1


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["code", "name", "rates"]
        depth = 2

