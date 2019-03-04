from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location


# Create your views here.

def start(request):

    all_images = Image.objects.all()
    return render(request,'index.html', {'all_images':all_images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
