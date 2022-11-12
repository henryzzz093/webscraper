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
    

admin.site.register(models.Apartments, ApartmentsAdmin)