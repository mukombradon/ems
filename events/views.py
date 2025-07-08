from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect,HttpResponseForbidden
from venues.models import Venue
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404, redirect
from .models import Event, Registration
from .utils import generate_ticket_pdf
from .models import *
from django.db.models import Q

# Create your views here.

@login_required(login_url='/users/login_user/')
def events(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


@transaction.atomic
@login_required(login_url='/users/login_user/')
def create_event(request):
    user = request.user
    if request.POST:
        title = request.POST["title"]
        short_description = request.POST["short_description"]
        long_description = request.POST["long_description"]
        event_date = request.POST["event_date"]
        event_time = request.POST["event_time"]
        capacity = request.POST["capacity"]
        location = request.POST["location"]
        category = request.POST["category"]
        get_images = request.FILES.getlist("image")
        venue_id = request.POST.get("venue_id")
        try:
            venue = Venue.objects.get(id=venue_id)
        except (Venue.DoesNotExist, ValueError, TypeError):
            venues = Venue.objects.all()
            return render(request, 'events/create_event.html', {
                'CATEGORY_CHOICES': Event.CATEGORY_CHOICES,
                'venues': venues,
                'form_error': 'Invalid venue selected. Please choose from the list.'
            })

        new_event = Event()
        new_event.actor = user
        new_event.title = title
        new_event.short_description = short_description
        new_event.long_description = long_description
        new_event.event_date = event_date
        new_event.event_time = event_time
        new_event.venue = venue
        new_event.capacity = capacity
        new_event.image = request.FILES['image']
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


@transaction.atomic
@login_required(login_url='/users/login_user/')
def edit_event(request, event_id):
    user = request.user
    get_event = Event.objects.get(id=event_id)

    if request.method == "POST":
        get_event.actor = user
        get_event.title = request.POST["title"]
        get_event.short_description = request.POST["short_description"]
        get_event.long_description = request.POST["long_description"]
        get_event.event_date = request.POST["event_date"]
        get_event.event_time = request.POST["event_time"]
        get_event.capacity = request.POST["capacity"]
        get_event.location = request.POST["location"]
        get_event.category = request.POST["category"]

        # Get venue_id from POST and validate it
        venue_id = request.POST.get("venue_id")
        try:
            venue = Venue.objects.get(id=venue_id)
            get_event.venue = venue
        except (Venue.DoesNotExist, ValueError, TypeError):
            venues = Venue.objects.all()
            return render(request, 'events/edit_event.html', {
                'get_event': get_event,
                'venues': venues,
                'form_error': 'Invalid venue selected. Please choose from the list.'
            })

        # Handle image uploads
        get_images = request.FILES.getlist("image")
        for image in get_images:
            new_image = EventImage()
            new_image.event = get_event
            new_image.image = image
            new_image.save()

        get_event.save()
        return HttpResponseRedirect('/events/events/')

    else:
        venues = Venue.objects.all()
        return render(request, 'events/edit_event.html', {
            'get_event': get_event,
            'venues': venues
        })


@login_required(login_url='/users/login_user/')
def event_details(request, event_id):
    user = request.user
    get_event = get_object_or_404(Event, id=event_id)
    get_venue = get_event.venue if get_event.venue else None
    event_image = EventImage.objects.filter(event=event_id)
    registered_event_ids = []
    if request.user.is_authenticated:
        registered_event_ids = Registration.objects.filter(user=request.user).values_list('event_id', flat=True)

    return render(request, 'events/event_details.html', {
        'get_event': get_event,
        'get_venue': get_venue,
        'event_image': event_image,
        'registered_event_ids': registered_event_ids
    })
#Event registration view
@login_required(login_url='/users/login_user/')
def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    registration, created = Registration.objects.get_or_create(user=request.user, event=event)
    if created:
        pdf = generate_ticket_pdf(registration)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=ticket_{registration.ticket_id}.pdf'
        return response
    return HttpResponse("Already registered", status=400)



@login_required(login_url='/users/login_user/')
def my_events(request):
    events = Event.objects.filter(actor=request.user)
    return render(request, 'events/my_events.html', {'events': events})


@login_required
def manage_attendees(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user != event.actor:
        return HttpResponse("Unauthorized", status=403)

    query = request.GET.get("q", "")
    attendees = Registration.objects.filter(event=event)

    if query:
        attendees = attendees.filter(
            Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
        )

    remaining_slots = event.capacity - attendees.count() if event.capacity else None

    return render(request, 'events/manage_attendees.html', {
        'event': event,
        'attendees': attendees,
        'remaining_slots': remaining_slots,
        'query': query,
    })


@login_required
def remove_attendee(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)

    if request.user != registration.event.actor:
        return HttpResponse("Unauthorized", status=403)

    registration.delete()
    return redirect('manage_attendees', event_id=registration.event.id)