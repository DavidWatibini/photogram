from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location


# Create your views here.

def start(request):

    all_images = Image.objects.all()
    return render(request,'index.html', {'all_images':all_images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
