from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile, Image,Comment

# Create your views here.
def home(request):
    photo = Image.objects.all()
    return render(request, 'instagram/home.html',{"photo":photo})

def search_results(request):
    if 'images' in request.GET["images"]:
        search_term = request.GET.get("images")
        searched_image = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"image": searched_image})
    else:
        message = "You haven't searched anything"
        return render(request,'instagram/search.html',{"message":message})
