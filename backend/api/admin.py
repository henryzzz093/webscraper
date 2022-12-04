from django.contrib import admin

from . import models


class ApartmentsAdmin(admin.ModelAdmin):
    list_display = [
        "company",
        "floorplan",
        "available",
        "bedrooms",
        "baths",
        "size",
        "rent",
        "date",
        "created_at",
        "updated_at",
    ]
    
class AirlineAdmin(admin.ModelAdmin):
    list_display = [
        "airline", 
        "departure_time",
        "destination_time",
        "price",
        "stops",
        "duration",
    ]
        


admin.site.register(models.Apartments, ApartmentsAdmin)
admin.site.register(models.Airline, AirlineAdmin)