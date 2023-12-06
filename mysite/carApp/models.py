from django.db import models

# Create your models here.
from django.db import models

class Car(models.Model):
    marque = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    version = models.CharField(max_length=50)
    note = models.FloatField(default=0.0)


    def __str__(self):
        return f"{self.year} {self.marque} {self.model}"