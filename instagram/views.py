from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.
def home(request):
    images = Image.objects.all()
    return HttpResponse(request, 'home.html')

def search_results(request):
    if 'images' in request.GET["images"]:
        search_term = request.GET.get("images")
        searched_image = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images": searched_image})
    else:
        message = "You haven't searched anything"
        return render(request,'search.html',{"message":message})
    