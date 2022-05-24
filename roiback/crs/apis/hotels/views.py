from django.http import JsonResponse, HttpResponse
from crs.models import Hotel, Room, Rate, Inventory
from django.views.generic import TemplateView
# from django.core.exceptions import ObjectDoesNotExist
# from django.views.decorators.csrf import csrf_exempt


class HotelView(TemplateView):

    def get(self, request, *args, **kwargs):
        h = Hotel.objects.all().order_by('name')
        h_codes = [hotel.code for hotel in h]
        # h_name = [hotel.__str__() for hotel in h]
        data = {
            "hotels": h_codes
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        hotel = Hotel(name=name)
        hotel.save()
        return JsonResponse(hotel.get_basic_data())


class HotelSingleViews(TemplateView):

    def get(self, request, *args, **kwargs):
        """Get hotel registry from an ID."""
        code = kwargs["code"]
        try:
            h = Hotel.objects.get(code=code)
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        return JsonResponse(h.get_basic_data())


    # def patch(self, request, *args, **kwargs):
    #     code = kwargs["code"]
    #     name = request.POST.get("name")
    #     h = Hotel.objects.get(id=code)
    #     Hotel.objects.filter(id=code).update(name=name)
    #     return JsonResponse(h.get_basic_data())

    def post(self, request, *args, **kwargs):
        """Update the hotel name."""
        code = kwargs["code"]
        name = request.POST.get("name")
        try:
            h = Hotel.objects.get(code=code)
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        Hotel.objects.filter(code=code).update(name=name)
        h.refresh_from_db()
        return JsonResponse(h.get_basic_data())

    def delete(self, request, *args, **kwargs):
        """Delete a hotel registry using an ID."""
        code = kwargs["code"]
        try:
            h = Hotel.objects.get(code=code)
        except Hotel.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        Hotel.objects.filter(code=code).delete()
        return JsonResponse(h.get_basic_data())
