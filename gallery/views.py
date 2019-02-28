from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.

def start(request):

    title =('Home - Intrest your life Today')

    return render(request, 'index.html',)
