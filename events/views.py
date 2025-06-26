from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect,HttpResponseForbidden
from venues.models import Venue
from django.contrib.auth.models import User, Group, Permission

from .models import *

# Create your views here.

@login_required(login_url='/users/login_user/')
def events(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})



@transaction.atomic
@login_required(login_url='/users/login/')
def create_event(request):
    user = request.user
    if request.POST:
        title = request.POST["title"]
        short_description = request.POST["short_description"]
        long_description = request.POST["long_description"]
        event_date = request.POST["event_date"]
        event_time = request.POST["event_time"]
        venue_id = request.POST["venue_id"]
        capacity = request.POST["capacity"]
        location = request.POST["location"]
        category = request.POST["category"]
        get_images = request.FILES.getlist("image")


        new_event = Event()
        new_event.actor = user
        new_event.title = title
        new_event.short_description = short_description
        new_event.long_description = long_description
        new_event.event_date = event_date
        new_event.event_time = event_time
        new_event.venue_id = venue_id
        new_event.capacity = capacity
        new_event.location = location
        new_event.category = category
        new_event.save()

        for image in get_images:
            new_image = EventImage()
            new_image.event = Event.objects.get(id=new_event.id)
            new_image.image = image
            new_image.save()

        return HttpResponseRedirect('/events/events/')

    else:
        venues = Venue.objects.all()  
        return render(request, 'events/create_event.html', {
            'CATEGORY_CHOICES': Event.CATEGORY_CHOICES,
            'venues': venues,
            })


from django.shortcuts import render

from django.shortcuts import render

def categories(request):
    categories = [
        {'name': 'Music', 'display': 'Music', 'icon': 'fa-music'},
        {'name': 'Technology', 'display': 'Technology', 'icon': 'fa-microchip'},
        {'name': 'Food & Drink', 'display': 'Food & Drink', 'icon': 'fa-utensils'},
        {'name': 'Business', 'display': 'Business', 'icon': 'fa-briefcase'},
        {'name': 'Art', 'display': 'Art', 'icon': 'fa-palette'},
        {'name': 'Sports', 'display': 'Sports', 'icon': 'fa-running'},
        {'name': 'Health & Wellness', 'display': 'Health & Wellness', 'icon': 'fa-heartbeat'},
        {'name': 'Education', 'display': 'Education', 'icon': 'fa-graduation-cap'},
        {'name': 'Science', 'display': 'Science', 'icon': 'fa-flask'},
        {'name': 'Entertainment/Gaming', 'display': 'Entertainment/Gaming', 'icon': 'fa-gamepad'},
        {'name': 'Travel', 'display': 'Travel', 'icon': 'fa-plane'},
        {'name': 'Fashion', 'display': 'Fashion', 'icon': 'fa-tshirt'},
        {'name': 'Film & Media', 'display': 'Film & Media', 'icon': 'fa-film'},
        {'name': 'Literature', 'display': 'Literature', 'icon': 'fa-book-open'},
        {'name': 'Theatre', 'display': 'Theatre', 'icon': 'fa-theater-masks'},
        {'name': 'Dance', 'display': 'Dance', 'icon': 'fa-shoe-prints'},
        {'name': 'Comedy', 'display': 'Comedy', 'icon': 'fa-grin-squint-tears'},
        {'name': 'Family & Kids', 'display': 'Family & Kids', 'icon': 'fa-child'}
    ]
    return render(request, 'events/categories.html', {'categories': categories})