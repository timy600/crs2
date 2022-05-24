from django.http import JsonResponse
from crs.models import Hotel, Room, Rate, Inventory
import uuid
from datetime import date


class InventoryService:

    # def book_room(self, room_code: uuid.uuid4, rate_code: uuid.uuid4, date: date):
    def book_room(self, room_code, rate_code, date):

        data = {
            "inventories": []
        }
        for rate in Rate.objects.filter(room=room_code):
            if rate.code != rate_code:
                inventories = Inventory.objects.filter(
                    date=date, rate=rate
                ).update(availability=False)
                # data["inventories"].append(inventories)
                inventories.refresh_from_db()
        return JsonResponse(data)
