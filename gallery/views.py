from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def start(request):

    title =('Home - Intrest your life Today')

    return render(request, 'index.html',)
