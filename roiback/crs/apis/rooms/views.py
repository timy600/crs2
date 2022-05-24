from django.http import JsonResponse, HttpResponse
from crs.models import Hotel, Room, Rate, Inventory
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
# from crs.apis.serializers import RoomSerializer
from crs.apis.model_serializers import RoomSerializer
from rest_framework.renderers import JSONRenderer


class RoomView(TemplateView):

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        rooms_codes = [room.code for room in rooms]
        data = {
            "rooms": rooms_codes
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        hotel_code = request.POST.get("hotel_code")
        try:
            hotel = Hotel.objects.get(code=hotel_code)
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Hotel Not Found')
        except ValidationError:
            return HttpResponse('Exception: Badly formed UUID')
        room = Room(name=name, hotel=hotel)
        print(room)
        room.save()
        return JsonResponse(room.get_basic_data())


class RoomHotelViews(TemplateView):
    def get(self, request, *args, **kwargs):
        """Get Room registries for a Hotel."""
        code = kwargs["code"]
        try:
            Hotel.objects.get(code=code)
            rooms = Room.objects.filter(hotel=code)
            room_codes = [room.code for room in rooms]
            data = {
                "rooms": room_codes
            }
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        except ValidationError:
            return HttpResponse('Exception: Badly formed UUID')
        except:
            return HttpResponse('Exception: Something went wrong')
        return JsonResponse(data)


class RoomSingleViews(TemplateView):

    def get(self, request, *args, **kwargs):
        """Get room registry from an ID."""
        code = kwargs["code"]
        try:
            r = Room.objects.get(code=code)
        except Room.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        return JsonResponse(r.get_basic_data())

    def post(self, request, *args, **kwargs):
        """Update the room name."""
        code = kwargs["code"]
        name = request.POST.get("name")
        try:
            r = Room.objects.get(code=code)
        except Room.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        Room.objects.filter(code=code).update(name=name)
        r.refresh_from_db()
        return JsonResponse(r.get_basic_data())

    def delete(self, request, *args, **kwargs):
        """Delete a room registry using an ID."""
        code = kwargs["code"]
        try:
            r = Room.objects.get(code=code)
        except Room.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        Room.objects.filter(code=code).delete()
        return JsonResponse(r.get_basic_data())


class RoomFullView(TemplateView):

    def get(self, request, *args, **kwargs):
        code = kwargs["code"]
        try:
            r = Room.objects.get(code=code)
        except Room.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        # serialized_room = RoomSerializer(r)
        # print(repr(serialized_room))
        # print(serialized_room.data)
        rates = Rate.objects.filter(room=code)
        rates_data = []
        for rate in rates:
            # print(rate)
            rate_dict = {
                "rate": rate.get_basic_data(),
                "inventories": [],
            }
            inventories = Inventory.objects.filter(rate=rate)
            for i in inventories:
                print(i)
                rate_dict["inventories"].append(i.get_basic_data())
            rates_data.append(rate_dict)

        data = {
            "room": r.get_basic_data(),
            "rates": rates_data
        }
        # json = JSONRenderer().render(serialized_room.data)
        # return json
        return JsonResponse(data)
