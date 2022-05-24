from django.http import JsonResponse, HttpResponse
from crs.models import Hotel, Room, Rate, Inventory
from django.views.generic import TemplateView
# from django.core.exceptions import ObjectDoesNotExist
# from django.views.decorators.csrf import csrf_exempt


class AvailabilityView(TemplateView):

    def get(self, request, *args, **kwargs):
        code = kwargs["code"]
        checkin_date = kwargs["checkin_date"]
        checkout_date = kwargs["checkout_date"]
        if checkout_date < checkin_date:
            return HttpResponse('Error: checkout must come after checkin')
        try:
            h = Hotel.objects.get(code=code)
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        rooms = Room.objects.filter(hotel=h)
        rooms_data = []
        for room in rooms:
            rates = Rate.objects.filter(room=room)
            rates_data = {}
            room_dict = {}
            room_dict[room.__str__()] = rates_data
            for rate in rates:
                rate_dict = {
                    "rate": rate.get_basic_data(),
                    "inventories": [],
                }
                inventories = Inventory.objects.filter(rate=rate)
                for i in inventories:
                    rate_dict["inventories"].append(i.get_basic_data())
                rates_data.append(rate_dict)

            rooms_data.append(room_dict)

        data = {
            "rooms": rooms_data
        }
        # json = JSONRenderer().render(serialized_room.data)
        # return json
        return JsonResponse(data)
"""
    def get(self, request, *args, **kwargs):
        code = kwargs["code"]
        checkin_date = kwargs["checkin_date"]
        checkout_date = kwargs["checkout_date"]
        try:
            h = Hotel.objects.get(code=code)
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        rooms = Room.objects.filter(hotel=h)

        rooms_data = []
        total_price = 0
        breakdown = {}
        for inventory:
            if
            breakdown[date_focus] = {

            }
        data = {
            "total": total_price,
            "breakdown": breakdown
        }
        return JsonResponse(data)
"""