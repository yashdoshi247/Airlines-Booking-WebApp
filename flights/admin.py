from django.contrib import admin
from .models import *

# Register your models here.

#Adding custom admin configurations
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("p_flights",)

admin.site.register(Flights, FlightAdmin)
admin.site.register(Airports)
admin.site.register(Passengers, PassengerAdmin)