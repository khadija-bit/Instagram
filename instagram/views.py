from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile, Image,Comment

# Create your views here.
def home(request):
    photo = Image.objects.all()
    comment = Comment.objects.all()
    return render(request, 'instagram/home.html',{"photo":photo})

def search_results(request):
    if 'image' in request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"image": searched_image})
    else:
        message = "You haven't searched anything"
        return render(request,'search.html',{"message":message})

def profile(request):
    current_user = request.user
    image = Image.objects.filter()