from django.contrib import admin

from .models import Hotel, Room, Rate, Inventory
# Register your models here.

# admin.site.register(Hotel)
# admin.site.register(Room)
# admin.site.register(Rate)
# admin.site.register(Inventory)


class RoomInline(admin.TabularInline):
    model = Room
    extra = 0


class HotelAdmin(admin.ModelAdmin):
    # fieldsets = [(None, {'fields': ['name']}),
    #              ('Room', {'fields': ['id'], 'classes':
    #                  ['collapse']})]
    fieldsets = []
    inlines = [RoomInline]


admin.site.register(Hotel, HotelAdmin)
