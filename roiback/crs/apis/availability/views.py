import datetime
from django.http import JsonResponse, HttpResponse
from crs.models import Hotel, Room, Rate, Inventory
from django.views.generic import TemplateView
from crs.apis.utils import validate_date
# from django.core.exceptions import ObjectDoesNotExist
# from django.views.decorators.csrf import csrf_exempt


class AvailabilityView(TemplateView):

    def get(self, request, *args, **kwargs):
        code = kwargs["code"]
        checkin_date = validate_date(kwargs["checkin_date"])
        checkout_date = validate_date(kwargs["checkout_date"])
        date_generated = [checkin_date + datetime.timedelta(days=x) for x in range(0, (checkout_date - checkin_date).days)]
        try:
            h = Hotel.objects.get(code=code)
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        rooms = Room.objects.filter(hotel=h)
        rooms_dict = {}
        for room in rooms:
            # rooms_dict.append()
            rates_dict = {}
            rates = Rate.objects.filter(room=room)
            for rate in rates:
                total_price = 0
                price = rate.price
                breakdown = {}
                for d in date_generated:
                    d = d.strftime("%Y-%m-%d")
                    inventories = Inventory.objects.filter(date=d, rate=rate)
                    for inv in inventories:
                        if inv.availability is False:
                            total_price = total_price + price
                            breakdown[d] = {
                                "price": price
                            }
                rates_dict[str(rate.code)] = {
                    "total": total_price,
                    "breakdown": [breakdown]
                }
            rooms_dict[str(room.code)] = {
                "rates": [rates_dict]
            }

        data = {
            "rooms": rooms_dict,
        }
        print(data)
        return JsonResponse(data)
