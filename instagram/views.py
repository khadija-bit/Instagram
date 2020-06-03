from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Profile, Image,Comment,NewsLetterEnts
from .forms import NewsLetterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    photo = Image.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterEnts(name = name,email = email)
            recipient.save()
            HttpResponseRedirect('home')
    else:
        form = NewsLetterForm()

    return render(request, 'instagram/home.html',{"photo":photo,"letterForm":form})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_image(search_term)
        message = f"{search_term}"
   
        return render(request,'instagram/search.html',{"message":message,"searched_image": searched_image})
        
    else:
        message = "You haven't searched anything"
        return render(request,'instagram/search.html',{"message":message})
