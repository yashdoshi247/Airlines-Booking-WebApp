from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
        "flights": Flights.objects.all()
    })

def flight_info(request, flight_id):
    flight=Flights.objects.get(pk=flight_id)
    return render(request,"flights/flight_info.html",{
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passengers.objects.exclude(p_flights=flight).all()
    })

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flights.objects.get(pk=flight_id)
        passenger = Passengers.objects.get(pk=int(request.POST['passenger_id']))
        passenger.p_flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight_info", args=(flight_id,)))
    

