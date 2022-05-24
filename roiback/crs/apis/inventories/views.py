from django.http import JsonResponse, HttpResponse
from crs.models import Hotel, Room, Rate, Inventory
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from crs.apis.utils import validate_date
from crs.apis.inventories.services import InventoryService


class InventoryView(TemplateView):

    def get(self, request, *args, **kwargs):
        inventories = Inventory.objects.all()
        inventory_data = [inventory.get_basic_data() for inventory in inventories]
        data = {
            "inventories": inventory_data
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        # price = request.POST.get("price")
        # allotment = request.POST.get("allotment")
        availability = request.POST.get("availability")
        date = request.POST.get("date")
        rate_code = request.POST.get("rate_code")
        try:
            rate = Rate.objects.get(code=rate_code)
            check_inventory = Inventory.objects.get(
                date=date,
                rate=rate
            )
            if check_inventory is not None:
                return HttpResponse("Inventory already exists for this date and rate.")
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Rate Not Found')
        except Inventory.DoesNotExist:
            print("Inventory to create")
        except ValidationError:
            return HttpResponse('Exception: Badly formed UUID')
        inventory = Inventory(
            availability=availability,
            date=date,
            rate=rate
        )
        inventory.save()
        # InventoryService.book_room(
        #     room_code=rate.room.room_code,
        #     rate_code=rate_code,
        #     date=date
        # )
        return JsonResponse(inventory.get_basic_data())


class InventoriesRateViews(TemplateView):
    def get(self, request, *args, **kwargs):
        """Get Inventory registries for a Rate."""
        code = kwargs["code"]
        try:
            Rate.objects.get(code=code)
            inventories = Inventory.objects.filter(rate=code)
            inventory_dataset = [inventory.get_basic_data() for inventory in inventories]
            data = {
                "inventories": inventory_dataset
            }
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        except ValidationError:
            return HttpResponse('Exception: Badly formed UUID')
        except:
            return HttpResponse('Exception: Something went wrong')
        return JsonResponse(data)


class InventorySingleViews(TemplateView):

    def get(self, request, *args, **kwargs):
        code = kwargs["code"]
        try:
            r = Rate.objects.get(code=code)
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        return JsonResponse(r.get_basic_data())

    def post(self, request, *args, **kwargs):
        rate_code = kwargs["rate_code"]
        date = request.POST.get("date")
        availability = request.POST.get("availability")
        try:
            rate = Rate.objects.get(code=rate_code)
            check_inventory = Inventory.objects.get(
                date=date,
                rate=rate
            )
            if check_inventory is not None:
                check_inventory.update(availability=availability)
                check_inventory.refresh_from_db()
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Rate Not Found')
        except Inventory.DoesNotExist:
            print("Inventory to create")
        except ValidationError:
            return HttpResponse('Exception: Badly formed UUID')
        inventory = Inventory(
            availability=availability,
            date=date,
            rate=rate
        )
        inventory.save()
        # InventoryService.book_room(
        #     room_code=rate.room.room_code,
        #     rate_code=rate_code,
        #     date=date
        # )
        return JsonResponse(inventory.get_basic_data())

    def delete(self, request, *args, **kwargs):
        code = kwargs["code"]
        try:
            r = Rate.objects.get(code=code)
        except Rate.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        Rate.objects.filter(code=code).delete()
        return JsonResponse(r.get_basic_data())
