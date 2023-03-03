from django.contrib import admin
from cars.models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    #fields = ['year', 'brand']
    fieldsets = [
        ('DATE INFO: ', {'fields': ['year']}),
        ('CAR INFO', {'fields': ['brand']})
    ]


admin.site.register(Car, CarAdmin)
