from django.db import models

# Create your models here.
class Airports(models.Model):
    city = models.CharField(max_length=65)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flights(models.Model):
    origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
class Passengers(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    p_flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

