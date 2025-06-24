from django.db import models
from django.contrib.auth.models import User, Group, Permission
# Create your models here.
from django.db import models
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator


from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    capacity = models.IntegerField()
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(blank=True,max_digits=2,decimal_places=1,default=1.0,validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])
    actor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)


    def __str__(self):
        return f"{self.name} - {self.city}, {self.country}"
        
class VenueImage(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='venue_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.venue.name}"
