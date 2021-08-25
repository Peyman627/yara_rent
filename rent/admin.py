from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name', 'price')
    list_filter = ('brand', )
    search_fields = ('name', 'brand')
    # date_hierarchy = 'created_time'
