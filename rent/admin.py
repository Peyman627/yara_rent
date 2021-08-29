from django.contrib import admin

from .models import Car, CarRent


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name', 'price')
    list_filter = ('brand', )
    search_fields = ('name', 'brand')
    date_hierarchy = 'created_time'


@admin.register(CarRent)
class CarRentAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'amount')
