from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Sum
# Create your views here.



def index(request):
	user = request.user
	
	return render(request, 'index.html', { })
