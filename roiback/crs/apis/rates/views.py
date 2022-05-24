from django.http import JsonResponse, HttpResponse
from crs.models import Hotel, Room, Rate
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from crs.apis.utils import check_type


class RateView(TemplateView):

    def get(self, request, *args, **kwargs):
        rates = Rate.objects.all()
        rates_codes = [rate.code for rate in rates]
        data = {
            "rates": rates_codes
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        print(name)
        price = float(request.POST.get("price"))
        print(price)
        check_type(price)
        room_code = request.POST.get("room_code")
        try:
            room = Room.objects.get(code=room_code)
        except Room.DoesNotExist:
            return HttpResponse('Exception: Room Not Found')
        except ValidationError:
            return HttpResponse('Exception: Badly formed UUID')
        rate = Rate(name=name, room=room, price=price)
        rate.save()
        return JsonResponse(rate.get_basic_data())


class RatesRoomViews(TemplateView):
    def get(self, request, *args, **kwargs):
        """Get Rate registries for a Room."""
        code = kwargs["code"]
        try:
            Room.objects.get(code=code)
            rates = Rate.objects.filter(room=code)
            rate_codes = [rate.code for rate in rates]
            data = {
                "rates": rate_codes
            }
        except Room.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        except ValidationError:
            return HttpResponse('Exception: Badly formed UUID')
        except:
            return HttpResponse('Exception: Something went wrong')
        return JsonResponse(data)


class RateSingleViews(TemplateView):

    def get(self, request, *args, **kwargs):
        """Get rate registry from an ID."""
        code = kwargs["code"]
        try:
            r = Rate.objects.get(code=code)
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        return JsonResponse(r.get_basic_data())

    def post(self, request, *args, **kwargs):
        """Update the rate price or name."""
        code = kwargs["code"]
        name = request.POST.get("name")
        price = request.POST.get("price")
        try:
            r = Rate.objects.get(code=code)
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        Rate.objects.filter(code=code).update(name=name, price=price)
        r.refresh_from_db()
        return JsonResponse(r.get_basic_data())

    def delete(self, request, *args, **kwargs):
        """Delete a rate registry using an ID."""
        code = kwargs["code"]
        try:
            r = Rate.objects.get(code=code)
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        Rate.objects.filter(code=code).delete()
        return JsonResponse(r.get_basic_data())
