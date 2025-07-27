

from django.contrib import admin
from .models import Pet, AdoptionRequest

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "age", "is_adopted", "vaccination_date")
    list_filter  = ("species", "is_adopted")
    search_fields = ("name", "microchip_number")

@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ("pet", "full_name", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("full_name", "email", "phone")
