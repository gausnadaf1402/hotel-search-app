from django.db import models

# Create your models here.

class Eminities(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_description=models.TextField()
    hotel_image=models.CharField(max_length=500)
    price=models.IntegerField()
    Eminities=models.ManyToManyField(Eminities)

    def __str__(self):
        return self.hotel_name