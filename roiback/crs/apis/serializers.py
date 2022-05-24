from rest_framework import serializers


class InventorySerializer(serializers.Serializer):
    availability = serializers.BooleanField()
    date = serializers.DateField()


class RateSerializer(serializers.Serializer):
    code = serializers.UUIDField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    inventories = InventorySerializer(many=True)


class RoomSerializer(serializers.Serializer):
    code = serializers.UUIDField()
    name = serializers.CharField()
    rates = RateSerializer(many=True)

