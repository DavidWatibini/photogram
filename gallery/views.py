from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location


# Create your views here.

def start(request):

    all_images = Image.objects.all()
    return render(request,'index.html', {'all_images':all_images})
