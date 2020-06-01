from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.
def home(request):
    images = Image.objects.all()
    return HttpResponse(request, 'home.html')
