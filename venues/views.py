from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect,HttpResponseForbidden

from django.contrib.auth.models import User, Group, Permission

from .models import *

# Create your views here.

@login_required(login_url='/users/login_user/')
def venues(request):
	venues = Venue.objects.all()
	return render(request, 'venues/venue_list.html', {'venues': venues})


@transaction.atomic
@login_required(login_url='/users/login/')
def create_venue(request):
	user = request.user
	if request.POST:
		name = request.POST["name"]
		address  = request.POST["address"]
		city = request.POST["city"]
		region = request.POST["region"]
		country = request.POST["country"]
		capacity= request.POST["capacity"]
		contact_email= request.POST["contact_email"]
		phone_number= request.POST["phone_number"]
		description = request.POST["description"]
		get_images= request.FILES.getlist("images")


		new_venue= Venue()
		new_venue.actor = user
		new_venue.name = name
		new_venue.address = address
		new_venue.city=city
		new_venue.region=region
		new_venue.country=country
		new_venue.capacity=capacity
		new_venue.contact_email=contact_email
		new_venue.phone_number=phone_number
		new_venue.description=description
		new_venue.save()

		for image in get_images:
			new_image = VenueImage()
			new_image.venue = Venue.objects.get(id = new_venue.id)
			new_image.image = image
			new_image.save()

		return HttpResponseRedirect('/venues/venues/')


	else:
		return render(request, "venues/add_venue.html")


@transaction.atomic
@login_required(login_url='/users/login_user/')
def edit_venue(request, venue_id):
	user = request.user
	get_venue = Venue.objects.get(id = venue_id)
	if request.POST:
		get_venue.actor = user
		get_venue.name = request.POST["name"]
		get_venue.address = request.POST["address"]
		get_venue.city = request.POST["city"]
		get_venue.region=request.POST["region"]
		get_venue.country=request.POST["country"]
		get_venue.capacity=request.POST["capacity"]
		get_venue.email = request.POST["contact_email"]
		get_venue.phone_number=request.POST["phone_number"]
		get_venue.description=request.POST["description"]
		get_venue.save()
		return HttpResponseRedirect('/venues/venues/')
		
	else:
		return render(request, 'venues/edit_venue.html', {'get_venue':get_venue})

@login_required(login_url='/users/login_user/')
def delete_venue(request, venue_id):
	get_venue = Venue.objects.get(id = venue_id)
	get_venue.delete()

	return HttpResponseRedirect('venues/venues')


@login_required(login_url='/users/login_user/')
def venue_details(request, venue_id):
	user = request.user
	get_venue = Venue.objects.get(id = venue_id)
	return render(request, 'venues/venue_details.html', {'get_venue':get_venue}) 
