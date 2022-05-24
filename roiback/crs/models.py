"""Models File"""

import uuid
from datetime import date
from django.db import models
from django.db.models.constraints import UniqueConstraint


class Hotel(models.Model):
    """Hotel Model."""
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    def get_basic_data(self):
        """Basic Data DTO."""
        response = {
            'name': self.name,
            'code': self.code
        }
        return response


class Room(models.Model):
    """Room Model."""
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    def get_basic_data(self):
        """Basic DTO."""
        response = {
            'name': self.name,
            'code': self.code,
            'hotel': self.hotel.name,
            'hotel_code': self.hotel.code
        }
        return response


class Rate(models.Model):
    """Rate Model."""
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def get_basic_data(self):
        """Basic DTO."""
        response = {
            'name': self.name,
            'price': self.price,
            'code': self.code,
            'room': self.room.name,
            'room_code': self.room.code
        }
        return response


class Inventory(models.Model):
    """Inventory Model."""

    class Meta:
        """Meta"""
        UniqueConstraint(fields=['rate', 'date'], name='id')
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    availability = models.BooleanField(default=True)
    # price = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)

    def get_basic_data(self):
        """Basic DTO."""
        response = {
            'availability': self.availability,
            # 'price': self.price,
            'date': self.date,
            'rate': self.rate.name,
            'rate_code': self.rate.code
        }
        return response
