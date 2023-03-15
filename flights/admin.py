from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Flights)
admin.site.register(Airports)
admin.site.register(Passengers)