from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
	return render(request, 'app/index.html')


def contact(request):
	return render(request, 'app/support.html')

def career(request):
	return render(request, 'app/career.html')

def apply(request):
	return render(request, 'app/apply.html')