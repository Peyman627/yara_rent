import humanize
from django.contrib import admin

from .models import Car, CarRent


class CarRentInline(admin.TabularInline):
    model = CarRent


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ('id', 'brand', 'name', 'get_price', 'get_color')
    list_display_links = ('id', 'name')
    list_filter = ('brand', )
    search_fields = ('name', 'brand')
    date_hierarchy = 'created_time'
    inlines = (CarRentInline, )

    @admin.display(description='price')
    def get_price(self, obj):
        return humanize.intword(obj.price)

    @admin.display(description='color')
    def get_color(self, obj):
        return obj.color if obj.color else 'Unknown'


@admin.register(CarRent)
class CarRentAdmin(admin.ModelAdmin):
    fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('user', 'car', 'amount')
    }), ('Time Information', {
        'fields': (('start_time', 'end_time'), ),
    }), (None, {
        'fields': ('is_enable', )
    }))
    list_display = ('username', 'car', 'get_amount', 'duration', 'is_enable')

    @admin.display
    def username(self, obj):
        return obj.user.user.username

    @admin.display(description='amount')
    def get_amount(self, obj):
        return humanize.intword(obj.amount)

    @admin.display
    def duration(self, obj):
        return humanize.precisedelta(obj.end_time - obj.start_time)
