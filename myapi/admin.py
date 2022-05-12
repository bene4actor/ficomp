from django.contrib import admin

from .models import Representative, Supply, Equipment, Order


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    ...


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    ...


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    ...


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...
