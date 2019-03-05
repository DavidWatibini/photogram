from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location


# Create your views here.

def start(request):

    index_images = Image.objects.all()
    return render(request,'index.html', {'index_images':index_images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html',{"message":message,"index_images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})
