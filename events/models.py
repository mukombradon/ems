from django.db import models

# Create your models here.
from django.db import models
from PIL import Image
from venues.models import Venue
from django.contrib.auth.models import User

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Music', 'Music'),
        ('Technology', 'Technology'),
        ('Food & Drink', 'Food & Drink'),
        ('Business', 'Business'),
        ('Art', 'Art'),
        ('Sports', 'Sports'),
        ('Health & Wellness', 'Health & Wellness'),
        ('Education', 'Education'),
        ('Science', 'Science'),
        ('Entertainment/Gaming', 'Entertainment/Gaming'),
        ('Travel', 'Travel'),
        ('Fashion', 'Fashion'),
        ('Social', 'Social'),
        ('Film & Media', 'Film & Media'),
        ('Literature', 'Literature'),
        ('Theatre', 'Theatre'),
        ('Dance', 'Dance'),
        ('Comedy', 'Comedy'),
        ('Family & Kids', 'Family & Kids'),]
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=110)
    long_description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    actor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)


    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.event.title}"